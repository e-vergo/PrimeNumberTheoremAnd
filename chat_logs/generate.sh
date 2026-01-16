#!/bin/bash
# Regenerate and style chat log HTML

cd "$(dirname "$0")"

# Clear cached HTML
rm -f *.html

# Regenerate HTML from JSONL
claude-code-log . -o all_sessions.html

# Apply styling
python3 style_logs.py *.html

# Open in browser
open all_sessions.html
