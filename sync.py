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
- Auto-Regenerates Showcase & Index:
    * Automatically rebuilds index.html and LINKS.md on every run, detecting:
      - Newly added repositories
      - Newly added index.html pages in previously non-demo folders
      - Updated templates and descriptions
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
GITHUB_REPO_OWNER = "hasanshahriar32"
GITHUB_REPO_NAME = "animated-template"
BASE_URL_PAGES = f"https://{GITHUB_REPO_OWNER}.github.io/{GITHUB_REPO_NAME}"
BASE_URL_SOURCE = f"https://github.com/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/tree/main"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
META_FILE = os.path.join(BASE_DIR, ".sync_metadata.json")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")
LINKS_FILE = os.path.join(BASE_DIR, "LINKS.md")

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
    "index.html",
    "LINKS.md",
    "__pycache__"
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

        copy_non_destructive(clone_dest, dest_path)
        status = "NEW" if is_new else "UPDATED"
        msg = "Cloned new repository" if is_new else "Updated files from upstream"
        return name, status, msg, repo_info.get("pushed_at")

def generate_showcase(remote_repos=None):
    """
    Regenerates index.html and LINKS.md dynamically from the current repository folders.
    Guarantees:
    - If a folder didn't have an index.html previously and now has one, it is detected immediately.
    - If a new repository was added, it is included.
    - Both Card Grid and Table View allow copying direct URLs in one click.
    """
    metadata = load_metadata()
    repo_map = {r["name"]: r for r in remote_repos} if remote_repos else {}

    items = []
    folders = sorted([
        d for d in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, d)) and d not in IGNORE_ENTRIES and not d.startswith(".")
    ])

    for folder in folders:
        folder_path = os.path.join(BASE_DIR, folder)
        has_demo = os.path.exists(os.path.join(folder_path, "index.html"))

        preview_img = ""
        previews_dir = os.path.join(folder_path, "previews")
        if os.path.exists(previews_dir):
            files = os.listdir(previews_dir)
            for cand in ["desktop.png", "desktop.webp", "scroll.gif", "phone.png"]:
                if cand in files:
                    preview_img = f"./{folder}/previews/{cand}"
                    break
            if not preview_img and files:
                preview_img = f"./{folder}/previews/{files[0]}"

        r_meta = repo_map.get(folder) or metadata.get(folder, {})
        desc = r_meta.get("description") or "Clean, animated responsive template for modern web projects."
        topics = r_meta.get("topics") or []

        category = "Website Template"
        if folder.startswith("awesome-") or "resources" in folder:
            category = "Curated List"
        elif "plugin" in folder or "mcp" in folder or "builder" in folder or folder in ("ui", "open-design"):
            category = "Developer Tool"

        demo_url = f"{BASE_URL_PAGES}/{folder}/" if has_demo else ""
        source_url = f"{BASE_URL_SOURCE}/{folder}"

        items.append({
            "id": folder,
            "title": folder.replace("-", " ").title(),
            "desc": desc,
            "has_demo": has_demo,
            "demo_url": demo_url,
            "source_url": source_url,
            "preview": preview_img,
            "category": category,
            "topics": topics[:4]
        })

    demos_count = sum(1 for i in items if i["has_demo"])
    tools_count = len(items) - demos_count

    # 1. Generate LINKS.md
    md_lines = [
        "# 📑 Template Index & Direct Links",
        "",
        f"> **Live Showcase Site**: [{BASE_URL_PAGES}]({BASE_URL_PAGES})",
        f"> Total Items: **{len(items)}** ({demos_count} Live Website Demos, {tools_count} Developer Tools & Lists)",
        "",
        "Quick navigation table with direct links to live demos and GitHub source directories.",
        "",
        "| # | Name | Category | Live Demo | Source Code | Description |",
        "|---|---|---|---|---|---|"
    ]

    for idx, item in enumerate(items, 1):
        demo_cell = f"[🌐 Live Demo]({item['demo_url']})" if item["has_demo"] else "*(Tool / Library)*"
        source_cell = f"[📁 Source]({item['source_url']})"
        clean_desc = item["desc"].replace("|", "\\|").replace("\n", " ")
        md_lines.append(
            f"| {idx} | **{item['title']}** | `{item['category']}` | {demo_cell} | {source_cell} | {clean_desc} |"
        )

    md_content = "\n".join(md_lines) + "\n"
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)

    # 2. Generate index.html
    items_json = json.dumps(items, ensure_ascii=False)

    html_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Animated Templates & Tools Showcase</title>
  <style>
    :root {
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f2937;
      --card-hover: #1e293b;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --accent: #6366f1;
      --accent-hover: #4f46e5;
      --tag-bg: #1e1b4b;
      --tag-text: #a5b4fc;
      --demo-bg: #10b981;
      --demo-hover: #059669;
      --copy-bg: #374151;
      --copy-hover: #4b5563;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 2rem 1.5rem;
    }
    .container {
      max-width: 1300px;
      margin: 0 auto;
    }
    header {
      text-align: center;
      margin-bottom: 2rem;
      padding: 2.5rem 1.5rem;
      background: linear-gradient(180deg, rgba(99, 102, 241, 0.15) 0%, rgba(9, 13, 22, 0) 100%);
      border-radius: 1rem;
      border: 1px solid rgba(99, 102, 241, 0.2);
    }
    h1 {
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      margin-bottom: 0.5rem;
      background: linear-gradient(135deg, #fff 30%, #a5b4fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    p.subtitle {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 700px;
      margin: 0 auto 1.5rem;
    }
    .badges {
      display: flex;
      gap: 0.75rem;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 1.5rem;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #1f2937;
      color: #e5e7eb;
      font-size: 0.825rem;
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      border: 1px solid #374151;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s;
    }
    .badge:hover {
      border-color: #6b7280;
    }
    .badge.accent {
      background: rgba(99, 102, 241, 0.25);
      border-color: rgba(99, 102, 241, 0.5);
      color: #c7d2fe;
    }
    .badge.action-btn {
      background: #312e81;
      border-color: #4f46e5;
      color: #e0e7ff;
      font-weight: 600;
    }
    .badge.action-btn:hover {
      background: #4338ca;
    }
    .controls {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2rem;
    }
    @media (min-width: 768px) {
      .controls {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
      }
    }
    .search-input {
      flex: 1;
      max-width: 450px;
      padding: 0.75rem 1.25rem;
      border-radius: 0.75rem;
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    }
    .view-controls {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      align-items: center;
    }
    .pill {
      padding: 0.5rem 0.9rem;
      border-radius: 0.5rem;
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.2s;
    }
    .pill:hover {
      color: var(--text);
      background: var(--card-hover);
    }
    .pill.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.5rem;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 0.875rem;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    }
    .card:hover {
      transform: translateY(-4px);
      border-color: #374151;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }
    .card-img-wrap {
      width: 100%;
      height: 190px;
      background: #0f172a;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      border-bottom: 1px solid var(--card-border);
      position: relative;
    }
    .card-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
      transition: transform 0.3s;
    }
    .card:hover .card-img {
      transform: scale(1.03);
    }
    .no-img {
      color: var(--text-muted);
      font-size: 0.85rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
    }
    .card-body {
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .card-category {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      font-weight: 700;
      margin-bottom: 0.4rem;
    }
    .card-title {
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--text);
    }
    .card-desc {
      color: var(--text-muted);
      font-size: 0.875rem;
      line-height: 1.45;
      margin-bottom: 1rem;
      flex: 1;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .tags {
      display: flex;
      gap: 0.4rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }
    .tag {
      background: var(--tag-bg);
      color: var(--tag-text);
      font-size: 0.725rem;
      padding: 0.2rem 0.55rem;
      border-radius: 0.35rem;
    }
    .card-footer {
      display: flex;
      gap: 0.5rem;
      margin-top: auto;
    }
    .btn {
      text-align: center;
      padding: 0.55rem 0.75rem;
      border-radius: 0.5rem;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      border: none;
      transition: all 0.2s;
    }
    .btn-demo {
      flex: 1.2;
      background: var(--demo-bg);
      color: #fff;
    }
    .btn-demo:hover {
      background: var(--demo-hover);
    }
    .btn-copy {
      background: var(--copy-bg);
      color: #e5e7eb;
    }
    .btn-copy:hover {
      background: var(--copy-hover);
    }
    .btn-source {
      background: #1f2937;
      color: #e5e7eb;
      border: 1px solid #374151;
    }
    .btn-source:hover {
      background: #374151;
    }
    .table-container {
      display: none;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 0.75rem;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }
    th, td {
      padding: 0.9rem 1.2rem;
      border-bottom: 1px solid var(--card-border);
    }
    th {
      background: #1e293b;
      color: #f3f4f6;
      font-weight: 600;
    }
    tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }
    .table-actions {
      display: flex;
      gap: 0.4rem;
    }
    .toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #10b981;
      color: white;
      padding: 0.75rem 1.5rem;
      border-radius: 0.5rem;
      font-weight: 600;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.3s ease;
      pointer-events: none;
      z-index: 1000;
    }
    .toast.show {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Animated Templates & Tools</h1>
      <p class="subtitle">An automated showcase of responsive, animated website templates and open-source tools with direct links and live demos.</p>
      <div class="badges">
        <span class="badge accent">__TOTAL_COUNT__ Repositories</span>
        <button class="badge action-btn" onclick="copyAllLinks()">📋 Copy All Demo Links</button>
        <a class="badge" href="./LINKS.md" target="_blank">📑 View LINKS.md Index ↗</a>
        <a class="badge" href="https://github.com/hasanshahriar32/animated-template" target="_blank">GitHub Repo ↗</a>
      </div>
    </header>

    <div class="controls">
      <input type="text" id="search" class="search-input" placeholder="Search templates, categories, keywords..." />
      <div class="view-controls">
        <div class="filter-pills" id="filters">
          <button class="pill active" data-cat="all">All (__TOTAL_COUNT__)</button>
          <button class="pill" data-cat="Website Template">Templates (__DEMO_COUNT__)</button>
          <button class="pill" data-cat="Developer Tool">Tools</button>
          <button class="pill" data-cat="Curated List">Lists</button>
        </div>
        <div style="border-left: 1px solid var(--card-border); height: 24px; margin: 0 0.5rem;"></div>
        <button class="pill" id="viewToggle" onclick="toggleView()">Switch to Table View 📑</button>
      </div>
    </div>

    <!-- Grid View -->
    <div class="grid" id="grid"></div>

    <!-- Table View -->
    <div class="table-container" id="tableContainer">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Category</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody id="tableBody"></tbody>
      </table>
    </div>
  </div>

  <div id="toast" class="toast">Link copied to clipboard!</div>

  <script>
    const items = __ITEMS_JSON__;
    const grid = document.getElementById('grid');
    const tableContainer = document.getElementById('tableContainer');
    const tableBody = document.getElementById('tableBody');
    const search = document.getElementById('search');
    const filterBtns = document.querySelectorAll('#filters .pill');
    const viewToggle = document.getElementById('viewToggle');
    const toast = document.getElementById('toast');

    let activeFilter = 'all';
    let searchQuery = '';
    let isTableView = false;

    function showToast(msg) {
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 2200);
    }

    function getAbsoluteUrl(folder) {
      const origin = window.location.origin;
      const pathname = window.location.pathname.replace(/\/index\.html$/, '').replace(/\/+$/, '');
      return `${origin}${pathname}/${folder}/index.html`;
    }

    function copyLink(folder, e) {
      if (e) e.stopPropagation();
      const url = getAbsoluteUrl(folder);
      navigator.clipboard.writeText(url).then(() => {
        showToast(`Copied live demo link for ${folder}!`);
      });
    }

    function copyAllLinks() {
      const demoItems = items.filter(i => i.has_demo);
      const list = demoItems.map(i => `${i.title}: ${getAbsoluteUrl(i.id)}`).join('\n');
      navigator.clipboard.writeText(list).then(() => {
        showToast(`Copied all ${demoItems.length} demo links to clipboard!`);
      });
    }

    function toggleView() {
      isTableView = !isTableView;
      if (isTableView) {
        grid.style.display = 'none';
        tableContainer.style.display = 'block';
        viewToggle.textContent = 'Switch to Card Grid 🎴';
      } else {
        grid.style.display = 'grid';
        tableContainer.style.display = 'none';
        viewToggle.textContent = 'Switch to Table View 📑';
      }
      render();
    }

    function render() {
      const q = searchQuery.toLowerCase().trim();
      const filtered = items.filter(item => {
        const matchesCat = activeFilter === 'all' || item.category === activeFilter;
        const matchesQuery = !q ||
          item.title.toLowerCase().includes(q) ||
          item.desc.toLowerCase().includes(q) ||
          item.topics.some(t => t.toLowerCase().includes(q));
        return matchesCat && matchesQuery;
      });

      if (isTableView) {
        tableBody.innerHTML = filtered.map((item, idx) => `
          <tr>
            <td>${idx + 1}</td>
            <td><strong>${item.title}</strong></td>
            <td><span class="tag">${item.category}</span></td>
            <td style="max-width: 450px;">${item.desc}</td>
            <td>
              <div class="table-actions">
                ${item.has_demo ? `
                  <a class="btn btn-demo" href="./${item.id}/index.html" target="_blank">Demo</a>
                  <button class="btn btn-copy" onclick="copyLink('${item.id}', event)">📋</button>
                ` : ''}
                <a class="btn btn-source" href="${item.source_url}" target="_blank">Source</a>
              </div>
            </td>
          </tr>
        `).join('');
      } else {
        grid.innerHTML = filtered.map(item => `
          <div class="card">
            <div class="card-img-wrap">
              ${item.preview ? `<img class="card-img" src="${item.preview}" alt="${item.title}" loading="lazy" />` : '<div class="no-img"><span>No Preview Available</span></div>'}
            </div>
            <div class="card-body">
              <div class="card-category">${item.category}</div>
              <h2 class="card-title">${item.title}</h2>
              <p class="card-desc" title="${item.desc}">${item.desc}</p>
              <div class="tags">
                ${item.topics.map(t => `<span class="tag">#${t}</span>`).join('')}
              </div>
              <div class="card-footer">
                ${item.has_demo ? `
                  <a class="btn btn-demo" href="./${item.id}/index.html" target="_blank">Live Demo ↗</a>
                  <button class="btn btn-copy" title="Copy Direct URL" onclick="copyLink('${item.id}', event)">📋 Copy Link</button>
                ` : ''}
                <a class="btn btn-source" href="${item.source_url}" target="_blank">Source</a>
              </div>
            </div>
          </div>
        `).join('');
      }
    }

    search.addEventListener('input', e => {
      searchQuery = e.target.value;
      render();
    });

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.dataset.cat;
        render();
      });
    });

    render();
  </script>
</body>
</html>
"""

    rendered_html = (
        html_template
        .replace("__ITEMS_JSON__", items_json)
        .replace("__TOTAL_COUNT__", str(len(items)))
        .replace("__DEMO_COUNT__", str(demos_count))
    )

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"✓ Regenerated index.html and LINKS.md ({len(items)} items, {demos_count} live demos).")

def main():
    force_all = "--force" in sys.argv
    regen_only = "--regen" in sys.argv

    if regen_only:
        print(f"Regenerating showcase files for {BASE_DIR}...")
        generate_showcase()
        return

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

        # Update metadata description/topics
        if name not in metadata:
            metadata[name] = {}
        metadata[name]["description"] = r.get("description") or ""
        metadata[name]["topics"] = r.get("topics") or []

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
                    metadata[name]["pushed_at"] = pushed_at
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

    # ALWAYS regenerate index.html and LINKS.md on every run
    # This guarantees that:
    # 1. Any new repository is added to the showcase
    # 2. If a folder previously had no index.html and now has one, its demo link is automatically enabled
    # 3. All links and counts are 100% current
    print("\nUpdating showcase index.html and LINKS.md...")
    generate_showcase(remote_repos)

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
