#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$ROOT/external/llm-sources"
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

clone_if_missing "https://github.com/wdndev/llm_interview_note.git" "llm_interview_note"
clone_if_missing "https://github.com/wdndev/tiny-llm-zh.git" "tiny-llm-zh"
clone_if_missing "https://github.com/wdndev/tiny-rag.git" "tiny-rag"
clone_if_missing "https://github.com/wdndev/tiny-mcp.git" "tiny-mcp"
clone_if_missing "https://github.com/wdndev/llama3-from-scratch-zh.git" "llama3-from-scratch-zh"

echo "LLM source mirrors ready under: $TARGET"
