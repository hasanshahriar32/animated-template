#!/usr/bin/env python3
"""
Sync Script for 8bsite Templates (Monorepo & GitHub Actions compatible)

Features:
- Fast: Uses GitHub API 'pushed_at' timestamps and local metadata (.sync_metadata.json)
        to only download/clone repositories that actually have new commits.
- Non-Destructive:
    * Never deletes any directory or file, even if removed from 8bsite's GitHub.
    * Preserves custom/local files and folders.
    * Only copies new or updated files over existing files.
- Monorepo Ready:
    * Excludes nested .git folders so the entire directory can be tracked in
      a single top-level Git repository and pushed to GitHub without issues.
- GitHub Actions Ready:
    * Automatically uses GITHUB_TOKEN if available (no rate limit issues).
    * Exit code 0 on success.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

TARGET_USER = "8bsite"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
META_FILE = os.path.join(BASE_DIR, ".sync_metadata.json")
IGNORE_ENTRIES = {
    os.path.basename(__file__),
    "update.sh",
    "sync.sh",
    ".sync_metadata.json",
    ".github",
    ".git",
    "README.md",
    ".gitignore",
    ".nojekyll",
    "index.html"
}

def load_metadata():
    if os.path.exists(META_FILE):
        try:
            with open(META_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_metadata(meta):
    try:
        with open(META_FILE, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"Warning: could not save metadata: {e}", file=sys.stderr)

def get_headers():
    headers = {
        "User-Agent": "8bsite-monorepo-sync",
        "Accept": "application/vnd.github.v3+json"
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def fetch_remote_repos(username):
    repos = []
    page = 1
    headers = get_headers()
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if not data:
                    break
                repos.extend(data)
                page += 1
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print("GitHub API rate limit reached.", file=sys.stderr)
            else:
                print(f"HTTP error fetching repos (page {page}): {e}", file=sys.stderr)
            break
        except Exception as e:
            print(f"Error fetching repos from GitHub: {e}", file=sys.stderr)
            break
    return repos

def copy_non_destructive(src_dir, dest_dir):
    """
    Copies new and updated files from src_dir to dest_dir.
    Ignores .git folder.
    NEVER deletes any file in dest_dir.
    """
    os.makedirs(dest_dir, exist_ok=True)
    for root, dirs, files in os.walk(src_dir):
        if ".git" in dirs:
            dirs.remove(".git")
        rel_path = os.path.relpath(root, src_dir)
        target_root = os.path.join(dest_dir, rel_path) if rel_path != "." else dest_dir
        os.makedirs(target_root, exist_ok=True)
        for f in files:
            src_file = os.path.join(root, f)
            dest_file = os.path.join(target_root, f)
            try:
                shutil.copy2(src_file, dest_file)
            except Exception as e:
                print(f"Warning: could not copy {src_file}: {e}", file=sys.stderr)

def sync_single_repo(repo_info, is_new):
    name = repo_info["name"]
    clone_url = repo_info["clone_url"]
    dest_path = os.path.join(BASE_DIR, name)

    with tempfile.TemporaryDirectory() as tmp_dir:
        clone_dest = os.path.join(tmp_dir, name)
        res = subprocess.run(
            ["git", "clone", "--depth", "1", clone_url, clone_dest],
            capture_output=True,
            text=True,
            timeout=180
        )
        if res.returncode != 0:
            return name, "ERROR", f"Git clone failed: {res.stderr.strip()}", None

        # Copy files non-destructively
        copy_non_destructive(clone_dest, dest_path)
        status = "NEW" if is_new else "UPDATED"
        msg = "Cloned new repository" if is_new else "Updated files from upstream"
        return name, status, msg, repo_info.get("pushed_at")

def main():
    force_all = "--force" in sys.argv
    print(f"Target directory: {BASE_DIR}")
    print(f"Fetching public repositories for user '{TARGET_USER}' ...")

    remote_repos = fetch_remote_repos(TARGET_USER)
    if not remote_repos:
        print("Failed to retrieve repositories list from GitHub. Aborting.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(remote_repos)} public repositories on GitHub.")

    metadata = load_metadata()
    tasks_to_run = []
    already_up_to_date = []

    for r in remote_repos:
        name = r["name"]
        pushed_at = r.get("pushed_at")
        dest_path = os.path.join(BASE_DIR, name)
        is_new = not os.path.exists(dest_path)

        last_pushed = metadata.get(name, {}).get("pushed_at")

        if not is_new and not force_all and last_pushed == pushed_at:
            already_up_to_date.append(name)
        else:
            tasks_to_run.append((r, is_new))

    print(f"Repositories to download/update: {len(tasks_to_run)}")
    print(f"Repositories already up-to-date: {len(already_up_to_date)}\n")

    summary = {
        "NEW": [],
        "UPDATED": [],
        "UP_TO_DATE": already_up_to_date,
        "PRESERVED": [],
        "ERROR": []
    }

    if tasks_to_run:
        with ThreadPoolExecutor(max_workers=6) as executor:
            future_to_repo = {
                executor.submit(sync_single_repo, r, is_new): r["name"]
                for (r, is_new) in tasks_to_run
            }
            for future in as_completed(future_to_repo):
                name, status, msg, pushed_at = future.result()
                summary[status].append((name, msg))
                if pushed_at and status in ("NEW", "UPDATED"):
                    metadata[name] = {"pushed_at": pushed_at}
                if status == "NEW":
                    print(f"[+] NEW:     {name} - {msg}")
                elif status == "UPDATED":
                    print(f"[↑] UPDATED: {name} - {msg}")
                elif status == "ERROR":
                    print(f"[!] ERROR:   {name} - {msg}", file=sys.stderr)

    # Save updated metadata
    save_metadata(metadata)

    # Check for preserved local folders that are not on GitHub
    local_entries = set(os.listdir(BASE_DIR)) - IGNORE_ENTRIES
    remote_names = {r["name"] for r in remote_repos}
    for item in sorted(local_entries - remote_names):
        if os.path.isdir(os.path.join(BASE_DIR, item)):
            summary["PRESERVED"].append(item)

    print("\n" + "=" * 55)
    print("Sync Summary:")
    print(f"  - Newly downloaded:       {len(summary['NEW'])}")
    print(f"  - Updated:                {len(summary['UPDATED'])}")
    print(f"  - Already up-to-date:     {len(summary['UP_TO_DATE'])}")
    print(f"  - Preserved local folders: {len(summary['PRESERVED'])}")
    if summary["ERROR"]:
        print(f"  - Errors:                 {len(summary['ERROR'])}")
    print("=" * 55)
    print("All operations completed non-destructively.")

if __name__ == "__main__":
    main()
