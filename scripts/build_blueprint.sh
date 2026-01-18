#!/bin/bash
# Build and serve the Prime Number Theorem blueprint locally
# Usage: ./scripts/build_blueprint.sh
#
# Prerequisites:
#   - Lean 4 and Lake installed
#   - leanblueprint fork (for side-by-side display):
#       pipx install git+https://github.com/e-vergo/leanblueprint.git
#   - TeX distribution (optional, for PDF generation)

set -e

cd "$(dirname "$0")/.."
PROJECT_ROOT=$(pwd)

# Add pipx leanblueprint venv to PATH for plastex
export PATH="$HOME/.local/pipx/venvs/leanblueprint/bin:$PATH"

echo "=== Prime Number Theorem Blueprint Builder ==="
echo ""

# Check dependencies
check_dependency() {
    if ! command -v "$1" &> /dev/null; then
        echo "ERROR: $1 is not installed."
        echo "$2"
        exit 1
    fi
}

check_dependency "lake" "Please install Lean 4 and Lake."
check_dependency "leanblueprint" "Install with: pipx install git+https://github.com/e-vergo/leanblueprint.git"

echo "=== Step 1: Updating dependencies ==="
lake update

echo ""
echo "=== Step 2: Fetching mathlib cache ==="
lake exe cache get || echo "Cache fetch completed (some files may have been skipped)"

echo ""
echo "=== Step 3: Building Lean project ==="
lake build

echo ""
echo "=== Step 4: Building blueprint data ==="
# Use :blueprintPlain to skip highlighting (SubVerso panics on some PNT code patterns)
lake build :blueprintPlain

echo ""
echo "=== Step 5: Building blueprint (web only) ==="
cd blueprint
# Skip PDF for now - \leanposition not yet defined for LaTeX
leanblueprint web

echo ""
echo "=== Done! ==="
echo ""
echo "Blueprint built successfully."
echo "  - Web: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server."
echo ""

# Open browser
(open "http://localhost:8000") &

leanblueprint serve
