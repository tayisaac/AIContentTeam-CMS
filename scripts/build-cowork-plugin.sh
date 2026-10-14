#!/usr/bin/env bash
# Builds dist/content-team-<version>.plugin for Cowork from plugins/content-team.
set -euo pipefail
cd "$(dirname "$0")/.."
VER=$(python3 -c "import json;print(json.load(open('plugins/content-team/.claude-plugin/plugin.json'))['version'])")
mkdir -p dist
OUT="$PWD/dist/content-team-$VER.plugin"
rm -f "$OUT"
(cd plugins/content-team && zip -qr "$OUT" . -x '.DS_Store' '*/.DS_Store')
echo "Built $OUT"
