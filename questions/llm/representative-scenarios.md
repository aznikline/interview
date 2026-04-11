# LLM 代表题清单

## 题目

如果只保最值得讲的一批 LLM 题，应该怎么选？

## 一句话回答

先保最能覆盖 `模型基础 / 架构与训练 / 对齐 / 推理 / RAG / Agent / 评估` 七类场景的题。不是题越多越好，而是每道题都能挂到真实工程链路上。

## 展开回答

| 场景 | 推荐代表题 | 你要练什么 |
| --- | --- | --- |
| 基础概念 | decoder-only、tokenizer、上下文窗口 | 统一术语和层次边界 |
| 架构与训练 | MHA/MQA/GQA、并行训练、数据质量 | 训练代价、通信、显存 |
| 对齐 | SFT、RLHF、DPO | 偏好学习和目标差异 |
| 推理 | KV Cache、TTFT/TPOT、dynamic batching | 延迟与吞吐 trade-off |
| RAG | chunking、Embedding、ReRank、多路召回 | 检索链路和答案质量 |
| Agent / MCP | 工具调用、状态管理、MCP server/client | 工程边界和可靠性 |
| 评估 | 幻觉、离线评测、在线评测 | 指标、闭环和优化方向 |

### 最小刷题路径

- 为什么大模型大多是 decoder-only？
- SFT、RLHF、DPO 区别是什么？
- KV Cache 为什么重要？
- TTFT、TPOT、throughput 分别是什么？
- RAG 为什么不能简单理解成向量库？
- Agent / MCP 在解决什么问题？
- 幻觉怎么评估和缓解？

## 面试官追问

- 为什么训练优化和推理优化不能混着讲？
- 为什么 RAG 仍然会产生幻觉？
- 为什么 Agent 难稳定？

## 易错点

- 只会背术语，不会讲工程链路
- 不会用指标说问题
- 不会区分模型问题、检索问题和系统工程问题

## 关联知识点

- [LLM 核心题清单](00-must-know.md)
- [LLM 高频题](high-frequency.md)
- [LLM 面试专题首页](../../docs/topics/llm/00-index.md)
- [LLM 21 天计划](../../tracks/llm-interview-21d/README.md)
