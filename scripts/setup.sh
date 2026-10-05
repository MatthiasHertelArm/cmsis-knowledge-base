#!/usr/bin/env bash
# Create a virtual environment and install the Python dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv .venv
. .venv/bin/activate
pip install -q -r requirements.txt
echo "Done. Activate with: . .venv/bin/activate"
