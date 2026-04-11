# LLM 核心题清单

## 题目

LLM 面试最应该优先准备哪些题，顺序应该怎么排？

## 一句话回答

先保整条主链路：`基础概念 -> 架构 -> 训练 -> 对齐 -> 推理 -> RAG / Agent -> 评估`。顺序上先保住高频术语和链路层次，再补工程实践和追问。

## 展开回答

### 第一层：必须先拿下的 10 题

- 为什么大模型大多是 decoder-only？
- tokenizer 在影响什么？
- MHA / MQA / GQA 怎么选？
- SFT、RLHF、DPO 分别在解决什么问题？
- 多维并行为什么必要？
- KV Cache 为什么重要？
- TTFT、TPOT、throughput 分别衡量什么？
- RAG 为什么不能简单理解成“向量库 + prompt”？
- Agent / MCP 在解决什么工程问题？
- 幻觉怎么评估和缓解？

### 1 分钟速答表

| 题目 | 最低合格回答 |
| --- | --- |
| 为什么大模型大多是 decoder-only？ | 因为自回归生成更适合开放式文本生成，训练和推理链路也更统一。 |
| SFT、RLHF、DPO 区别是什么？ | SFT 做监督拟合，RLHF 引入偏好奖励，DPO 用更直接的偏好优化替代显式 reward model。 |
| KV Cache 为什么重要？ | 因为 decode 阶段重复利用历史 key/value，能显著减少重复计算，但会增加显存占用。 |
| TTFT、TPOT、throughput 分别是什么？ | TTFT 是首 token 时间，TPOT 是后续 token 速度，throughput 是整体吞吐，三者经常互相牵制。 |
| RAG 为什么不能简单理解成向量库？ | 因为真正效果取决于切块、召回、重排、上下文预算和答案生成协同。 |
| Agent / MCP 在解决什么问题？ | 它们把模型从“纯生成器”扩展成“可调用工具和外部系统的执行器”，但也引入状态、安全和观测复杂度。 |

## 面试官追问

- 为什么 decoder-only 适合 LLM？
- 为什么 dynamic batching 有用但也危险？
- 为什么 RLHF 不等于万能对齐？
- 为什么 Agent 一上线就变复杂？

## 易错点

- 只会背术语，不会讲层次
- 不会把训练、推理、RAG、Agent 串成一条线
- 不会讲指标和工程代价

## 关联知识点

- [LLM 面试专题首页](../../docs/topics/llm/00-index.md)
- [LLM 高频题](high-frequency.md)
- [LLM 代表题清单](representative-scenarios.md)
- [LLM 21 天计划](../../tracks/llm-interview-21d/README.md)
- [LLM 压测包](../../practice/drills/llm-pressure-pack.md)
