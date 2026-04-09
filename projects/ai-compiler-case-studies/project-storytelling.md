# AI 编译器项目表达稿

## 这份文档解决什么问题

很多人会原理，但不会讲项目。AI 编译器面试尤其容易出现“会背框架，不会讲优化闭环”。

这份稿子给你一个统一表达框架。

## 统一表达框架

### 1. 背景

- 目标模型是什么
- 目标硬件是什么
- 优化目标是什么：吞吐、延迟、显存还是成本

### 2. 问题

- 瓶颈在图级、kernel 级还是 runtime 级
- 是 compute bound 还是 memory bound
- 具体指标多差

### 3. 方案

- 做了哪些编译优化：fusion、layout、lowering、kernel selection
- 做了哪些 runtime 优化：batching、memory planning、stream scheduling
- 为什么这些优化适合当前 workload

### 4. 结果

- TTFT 提升多少
- TPOT 提升多少
- 吞吐提升多少
- 显存占用变化多少
- P99 延迟是否变差

### 5. 复盘

- 哪些优化有效
- 哪些优化离线有效、线上一般
- 如果重做一次会如何调整

## 一段可直接口述的模板

```text
我们当时优化的是一个典型的 LLM 推理链路，目标不是纯追求 benchmark，而是在线服务下的低延迟和稳定吞吐。
先做 profiling 之后，我们发现主要瓶颈不在单个算子本身，而在 decode 阶段的 memory bound 行为、kernel launch overhead 和 runtime 调度不稳定。
所以方案上分成两层：编译器层做 fusion、layout 优化和更合适的 kernel 选择，runtime 层做动态 batch、memory planning 和 fallback 路径收敛。
最后结果不是只看平均吞吐，我们重点看了 TTFT、TPOT 和 P99。最终吞吐提升了 X%，TTFT 降了 Y%，但我们也发现某些 aggressive fusion 虽然 benchmark 更好，线上 P99 反而变差，所以最后保留的是更稳的一版。
```

## 常见错误

- 只讲“用了 Triton / TVM / XLA”
- 不讲指标
- 不讲 workload 特征
- 不讲为什么线上和离线效果不同

