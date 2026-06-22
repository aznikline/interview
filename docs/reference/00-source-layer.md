# 参考源总目录

## 说明

这个仓库分成两层：

1. `手册整合层`
   也就是 `docs/topics`、`questions`、`tracks`、`practice` 这些内容。这里的正文以原创整理、结构化重写和训练路线为主。

2. `原始参考层`
   也就是外部原始仓库的完整目录。这些仓库**不进 git**，而是通过 bootstrap 脚本以 `--depth=1` clone 到 `external/` 下，保持原始目录结构，避免“只剩二手摘要看不到源头”，同时不让 clone 变重。

这两层不是互相替代，而是互相配合：

- 手册层负责“怎么学、怎么练、怎么答”
- 参考层负责“原始章节、源码、项目实践、完整目录”

## 拉取原始参考仓库

首次使用前先跑 bootstrap 脚本（`external/` 已在 `.gitignore`，不会污染工作区）：

```bash
bash scripts/bootstrap_llm_sources.sh        # LLM / RAG / MCP / 从零实现
bash scripts/bootstrap_ai_infra_sources.sh   # CUDA / AI Infra / 框架实现
```

脚本会在 `external/llm-sources/` 与 `external/ai-infra-sources/` 下放对应仓库。

## 当前已接入的原始参考仓库

### 01. LLM / RAG / MCP / 从零实现 → `external/llm-sources/`

- [llm_interview_note](../../external/llm-sources/llm_interview_note)
- [tiny-llm-zh](../../external/llm-sources/tiny-llm-zh)
- [tiny-rag](../../external/llm-sources/tiny-rag)
- [tiny-mcp](../../external/llm-sources/tiny-mcp)
- [llama3-from-scratch-zh](../../external/llm-sources/llama3-from-scratch-zh)

### 02. CUDA / AI Infra / 框架实现 → `external/ai-infra-sources/`

- [ai-infra-hpc](../../external/ai-infra-sources/ai-infra-hpc)
- [OriginDL](../../external/ai-infra-sources/OriginDL)

> 这些链接在跑过 bootstrap 脚本后才会有效；未拉取时目录为空。

## 推荐使用方式

### 如果你要系统学习

先走手册层：

- [Start Here](../START-HERE.md)
- [总路线图](../roadmap/00-overview.md)
- 对应领域的 `专题首页 -> 核心题清单 -> 代表题清单 -> 路线 -> 压测包`

### 如果你要看完整原始目录

先跑 bootstrap 脚本拉取，再走参考层：

- [LLM 参考源索引](01-llm-source-index.md)
- [AI Infra 参考源索引](02-ai-infra-source-index.md)
- [LLM 章节树](03-llm-reference-tree.md)
- [AI Infra 章节树](04-ai-infra-reference-tree.md)
- [手册层与原始层映射](05-handbook-to-reference-map.md)
