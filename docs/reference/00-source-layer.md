# 参考源总目录

## 说明

这个仓库现在分成两层：

1. `手册整合层`
   也就是 `docs/topics`、`questions`、`tracks`、`practice` 这些内容。这里的正文以原创整理、结构化重写和训练路线为主。

2. `原始参考层`
   也就是 `references/` 目录。这里直接以 submodule 的方式挂接外部仓库，保持原始目录结构，避免“只剩二手摘要看不到源头”。

这两层不是互相替代，而是互相配合：

- 手册层负责“怎么学、怎么练、怎么答”
- 参考层负责“原始章节、源码、项目实践、完整目录”

## 当前已接入的原始参考仓库

### 01. LLM / RAG / MCP / 从零实现

- [llm_interview_note](/Users/wizout/op/interview/references/llm_interview_note)
- [tiny-llm-zh](/Users/wizout/op/interview/references/tiny-llm-zh)
- [tiny-rag](/Users/wizout/op/interview/references/tiny-rag)
- [tiny-mcp](/Users/wizout/op/interview/references/tiny-mcp)
- [llama3-from-scratch-zh](/Users/wizout/op/interview/references/llama3-from-scratch-zh)

### 02. CUDA / AI Infra / 框架实现

- [ai-infra-hpc](/Users/wizout/op/interview/references/ai-infra-hpc)
- [OriginDL](/Users/wizout/op/interview/references/OriginDL)

## 推荐使用方式

### 如果你要系统学习

先走手册层：

- [Start Here](/Users/wizout/op/interview/docs/START-HERE.md)
- [总路线图](/Users/wizout/op/interview/docs/roadmap/00-overview.md)
- 对应领域的 `专题首页 -> 核心题清单 -> 代表题清单 -> 路线 -> 压测包`

### 如果你要看完整原始目录

直接走参考层：

- [LLM 参考源索引](/Users/wizout/op/interview/docs/reference/01-llm-source-index.md)
- [AI Infra 参考源索引](/Users/wizout/op/interview/docs/reference/02-ai-infra-source-index.md)

### 如果你要重新拉取外部仓库

- [bootstrap_llm_sources.sh](/Users/wizout/op/interview/scripts/bootstrap_llm_sources.sh)
- [bootstrap_ai_infra_sources.sh](/Users/wizout/op/interview/scripts/bootstrap_ai_infra_sources.sh)
