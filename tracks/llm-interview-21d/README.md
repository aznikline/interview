# LLM 21 天计划

适合：

- 想系统补齐大模型面试主线
- 需要把 `llm_interview_note + tiny-llm-zh + tiny-rag + tiny-mcp` 接成可执行路线
- 目标岗位是 LLM 算法、应用工程、平台工程、推理优化

## Week 1：基础、架构、训练

### Day 1-2

- [LLM 基础与术语](../../docs/topics/llm/01-llm-foundations.md)
- [LLM 核心题清单](../../questions/llm/00-must-know.md)

### Day 3-4

- [LLM 架构与训练](../../docs/topics/llm/02-llm-architecture-and-training.md)
- 对照 `external/llm-sources/llm_interview_note/02.大语言模型架构`

### Day 5-7

- 对照 `external/llm-sources/tiny-llm-zh/doc`
- 关注 tokenizer、训练参数、数据处理

## Week 2：推理、Serving、评估

### Day 8-10

- [LLM 推理与 Serving](../../docs/topics/llm/03-llm-inference-and-serving.md)
- 对照 `external/llm-sources/llm_interview_note/06.推理`

### Day 11-12

- 对照 `external/llm-sources/llama3-from-scratch-zh`
- 关注模型实现和 attention / rope / rmsnorm

### Day 13-14

- [RAG、Agent、MCP 与评估](../../docs/topics/llm/04-rag-agent-eval.md)
- 对照 `external/llm-sources/llm_interview_note/09.大语言模型评估`

## Week 3：RAG / Agent / MCP / 项目表达

### Day 15-17

- 对照 `external/llm-sources/tiny-rag/doc`
- 练检索、重排、多路召回

### Day 18-19

- 对照 `external/llm-sources/tiny-mcp/docs`
- 练 MCP server/client、工具调用、流程边界

### Day 20-21

- 跑 [LLM 压测包](../../practice/drills/llm-pressure-pack.md)
- 整理自己的项目表达和弱项清单

## 最小验收标准

- 至少 `10` 个 LLM 高频问题能稳定先给结论
- 至少 `3` 条工程链路能讲清楚 trade-off
- 至少 `1` 个训练 / 推理 / RAG / Agent 项目故事能讲顺
