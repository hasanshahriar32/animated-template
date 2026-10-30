#!/usr/bin/env bash
# Update script for 8bsite templates
# Non-destructive updater & downloader

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/sync.py" "$@"
