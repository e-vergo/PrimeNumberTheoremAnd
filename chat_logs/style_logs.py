#!/usr/bin/env python3
"""
Post-processor for claude-code-log HTML output.
Removes emojis and applies custom styling.
"""

import re
import sys
from pathlib import Path

# Emoji replacements - emoji to clean text
EMOJI_REPLACEMENTS = [
    (r'🤷\s*User', 'User'),
    (r'🤖\s*Assistant', 'Assistant'),
    (r'🛠️\s*Tool Use', 'Tool'),
    (r'🛠️\s*Tool', 'Tool'),
    (r'🧰\s*Tool Result', 'Result'),
    (r'💭\s*Thinking', 'Thinking'),
    (r'⚙️\s*System', 'System'),
    (r'🖼️\s*Image[s]?', 'Image'),
    (r'🔗\s*Sub-assistant', 'Sub-agent'),
    (r'🗓️', ''),
    (r'🔍', ''),
    (r'ℹ️\s*', 'Info: '),
    (r'⚠️\s*', 'Warning: '),
    (r'❌\s*', 'Error: '),
    (r'📝\s*', ''),
    (r'🤖\s*', ''),
    (r'✨\s*', ''),
    (r'🎯\s*', ''),
]

# CSS overrides
CUSTOM_CSS = """
/* Floating button icons */
.scroll-top.floating-btn::before {
    content: "\\2191";
    font-size: 1.4em;
    font-weight: bold;
}
.toggle-details.floating-btn::before {
    content: "\\00B1";
    font-size: 1.4em;
    font-weight: bold;
}
.filter-messages.floating-btn::before {
    content: "\\2315";
    font-size: 1.2em;
}
.timeline-toggle.floating-btn::before {
    content: "\\2630";
    font-size: 1.2em;
}

/* Light blue gradient background */
body {
    background: linear-gradient(90deg, #e8feff, #cafbff) !important;
    background-attachment: fixed !important;
}

/* Make chat cards opaque */
.message {
    background-color: #ffffff !important;
}
"""


def process_html(content: str) -> str:
    """Remove emojis and apply custom styling."""

    # 1. Apply specific emoji replacements
    for pattern, replacement in EMOJI_REPLACEMENTS:
        content = re.sub(pattern, replacement, content)

    # 2. Inject custom CSS before </style>
    content = content.replace('</style>', CUSTOM_CSS + '\n</style>')

    # 3. Clean up any remaining standalone emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F700-\U0001F77F"  # alchemical
        "\U0001F780-\U0001F7FF"  # geometric shapes extended
        "\U0001F800-\U0001F8FF"  # supplemental arrows-c
        "\U0001F900-\U0001F9FF"  # supplemental symbols & pictographs
        "\U0001FA00-\U0001FA6F"  # chess symbols
        "\U0001FA70-\U0001FAFF"  # symbols & pictographs extended-a
        "\U00002702-\U000027B0"  # dingbats
        "\U0000FE00-\U0000FE0F"  # variation selectors
        "\U0001F1E0-\U0001F1FF"  # flags
        "]+",
        flags=re.UNICODE
    )
    content = emoji_pattern.sub('', content)

    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python style_logs.py <html_file> [<html_file2> ...]")
        print("       python style_logs.py chat_logs/*.html")
        sys.exit(1)

    for filepath in sys.argv[1:]:
        path = Path(filepath)
        if not path.exists():
            print(f"Skipping {filepath}: file not found")
            continue
        if path.suffix != '.html':
            print(f"Skipping {filepath}: not an HTML file")
            continue

        print(f"Processing {filepath}...")
        content = path.read_text(encoding='utf-8')
        processed = process_html(content)
        path.write_text(processed, encoding='utf-8')
        print(f"  Done: {filepath}")

    print("\nAll files processed.")


if __name__ == '__main__':
    main()
