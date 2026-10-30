# 8bsite Templates Collection

A collection of free website templates and developer tools mirrored from [github.com/8bsite](https://github.com/8bsite).

## Automated Sync with GitHub Actions

This repository is kept up to date automatically:
- **Daily Cron**: Automatically checks for updates and newly published repositories daily at 04:00 UTC.
- **Manual Trigger**: Can be run anytime via the **Actions** tab by selecting `Sync Templates from 8bsite` and clicking **Run workflow**.

## Non-Destructive Behavior
- **Never deletes** any template folder or file (even if removed from upstream).
- **Preserves** all local custom files and modifications.
- Automatically detects new repositories and adds them to this collection.

## Local Usage
To run the sync locally on your machine:
```bash
./update.sh
```
*(or `python3 sync.py`)*
