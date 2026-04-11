# LLM 面试专题首页

## 1 分钟速答

LLM 面试不是只问 Transformer 结构，也不是只问推理框架。真正高频的问题会覆盖一整条链路：`基础概念 -> 模型架构 -> 数据与训练 -> SFT / 对齐 -> 推理与 Serving -> RAG / Agent -> 评估与应用`。准备这条主线时，不能只背术语，必须能讲清层次边界、核心瓶颈、指标和 trade-off。

## 核心机制

### 推荐学习顺序

1. 基础概念与术语
2. 架构与训练
3. 推理与 Serving
4. RAG / Agent / MCP / 评估
5. 项目实践与真实面试题

### 必读文档

- [01-llm-foundations.md](/Users/wizout/op/interview/docs/topics/llm/01-llm-foundations.md)
- [02-llm-architecture-and-training.md](/Users/wizout/op/interview/docs/topics/llm/02-llm-architecture-and-training.md)
- [03-llm-inference-and-serving.md](/Users/wizout/op/interview/docs/topics/llm/03-llm-inference-and-serving.md)
- [04-rag-agent-eval.md](/Users/wizout/op/interview/docs/topics/llm/04-rag-agent-eval.md)
- [05-llm-local-source-map.md](/Users/wizout/op/interview/docs/topics/llm/05-llm-local-source-map.md)

### 学完后应该具备什么能力

- 能把 `预训练 / SFT / RLHF / DPO / 推理 / RAG / Agent` 串成一条链路
- 能解释 `KV Cache / TTFT / TPOT / 吞吐 / 幻觉 / 检索 / 工具调用` 这些高频概念
- 能把 `llm_interview_note + tiny-llm-zh + tiny-rag + tiny-mcp + llama3-from-scratch-zh` 这些本地参考仓库映射到自己的学习路线

## 高频问法

- 为什么大模型大多是 decoder-only？
- SFT、RLHF、DPO 分别在解决什么问题？
- KV Cache 为什么重要？
- RAG 为什么不能简单理解成“向量库 + prompt”？
- Agent 和 MCP 为什么会把工程复杂度拉上来？

## 深挖与误区

- 不要只会背 Transformer 结构，不会讲训练和推理代价
- 不要把 RAG 讲成“接个向量库”就结束
- 不要把 Agent 讲成 workflow 花活，不讲工具调用边界和观测

## 下一步

- 刷 [LLM 核心题清单](/Users/wizout/op/interview/questions/llm/00-must-know.md)
- 刷 [LLM 代表题清单](/Users/wizout/op/interview/questions/llm/representative-scenarios.md)
- 跑 [LLM 21 天计划](/Users/wizout/op/interview/tracks/llm-interview-21d/README.md)
- 跑 [LLM 压测包](/Users/wizout/op/interview/practice/drills/llm-pressure-pack.md)
