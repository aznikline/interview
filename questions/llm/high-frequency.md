# LLM 高频题

## 题目

为什么大模型大多采用 decoder-only 架构？

## 一句话回答

因为 decoder-only 更适合自回归生成任务，训练目标统一，推理链路清晰，也更容易围绕生成场景做工程优化。

## 展开回答

- 自回归目标天然适配生成式任务
- 结构上更统一，工程生态成熟
- 与 KV Cache、推理优化链路适配度高

## 面试官追问

- encoder-decoder 为什么不占主流？
- decoder-only 在长上下文下有什么代价？

---

## 题目

KV Cache 为什么重要？

## 一句话回答

因为 decode 阶段会反复利用历史 token 的 key/value，如果不缓存，计算会被重复放大。

## 展开回答

- prefill 和 decode 阶段成本结构不同
- KV Cache 用空间换时间
- 代价是显存占用、cache 管理和批调度复杂度

## 面试官追问

- KV Cache 为什么会影响 batch？
- 为什么 decode 常常 memory bound？

---

## 题目

RAG 为什么不能简单理解成“检索 + prompt”？

## 一句话回答

因为真正效果取决于切块、召回、重排、上下文预算和答案生成协同，不是把文档塞进 prompt 就结束。

## 展开回答

- chunking 影响检索粒度
- embedding 和 ReRank 决定召回质量
- context budget 决定最终能放多少有效信息

## 面试官追问

- ReRank 的价值是什么？
- 多路召回什么时候值得做？
