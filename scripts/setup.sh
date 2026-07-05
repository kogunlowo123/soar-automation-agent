#!/bin/bash
set -euo pipefail
echo "Setting up SOAR Automation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
