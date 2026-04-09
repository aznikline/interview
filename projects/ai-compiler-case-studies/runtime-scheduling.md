# 项目案例：推理 Runtime 调度

## 场景

当模型编译产物已经固定后，线上性能仍然可能主要受 runtime 调度影响，例如 batch 拼接、stream 分配、内存复用和 fallback 路径。

## 核心问题

- 延迟优先还是吞吐优先
- prefill 和 decode 是否拆开调度
- 动态 batch 上限如何确定
- fallback 到通用 kernel 的频率是否过高

## 关键抓手

- 观察 TTFT、TPOT、P99 延迟、tokens/s
- 区分 compute bound 和 memory bound
- 根据 workload 选择更保守或更激进的批处理策略

## 面试表达重点

- 编译器不解决所有问题，runtime 决定在线执行效果
- 调度优化要围绕指标，不是围绕“更复杂的策略”
- 解释为什么某些优化在离线 benchmark 有效，但在线服务效果一般

