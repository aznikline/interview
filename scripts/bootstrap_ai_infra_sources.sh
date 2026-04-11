#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$ROOT/external/ai-infra-sources"
mkdir -p "$TARGET"

clone_if_missing() {
  local repo="$1"
  local name="$2"
  if [ -d "$TARGET/$name/.git" ]; then
    echo "exists: $name"
  else
    git clone --depth=1 "$repo" "$TARGET/$name"
  fi
}

clone_if_missing "https://github.com/jinbooooom/ai-infra-hpc.git" "ai-infra-hpc"
clone_if_missing "https://github.com/jinbooooom/OriginDL.git" "OriginDL"

echo "AI Infra source mirrors ready under: $TARGET"
