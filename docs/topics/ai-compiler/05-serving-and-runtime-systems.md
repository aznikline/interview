# Serving Runtime 与在线调度

## 1 分钟速答

AI 编译器在面试里如果只讲 compile time，通常是不够的。大模型推理和在线 serving 场景里，很多关键问题都出现在 runtime：`dynamic batching`、`KV cache`、`prefill/decode 分离`、`admission control`、`调度与吞吐/延迟权衡`。

## 核心机制

### 为什么 runtime 变得这么重要

静态编译优化很强，但在线 serving 有大量运行时变量：

- 请求长度不一样
- batch 形状不稳定
- 资源压力动态变化
- tail latency 有 SLA

这些问题不能完全在 compile time 决定，所以 runtime 负责很多“最后一公里”的决策。

### Dynamic Batching

这是最常见的 runtime 话题之一。

目标：

- 提高设备利用率
- 降低空跑

代价：

- 等待更多请求会增加 TTFT
- batch 太大又可能拖慢 decode 阶段

所以 runtime 的本质是平衡吞吐和延迟。

### KV Cache

KV cache 是大模型推理里最典型的内存与调度问题：

- 占用显存
- 影响 batch 拼接
- 影响请求调度和回收策略

如果不会讲 KV cache，很多 runtime 问题都接不住。

### Prefill / Decode 分离

这类问题常被问，是因为两阶段瓶颈不同：

- prefill 更偏算力
- decode 更偏 memory bound

因此调度、kernel 选择、batch 策略都可能不同。

## 高频问法

- dynamic batching 为什么不是越大越好？
- KV cache 为什么会成为 serving 瓶颈？
- prefill 和 decode 为什么经常分开优化？
- runtime 为什么不能完全被 compiler 替代？
- admission control 为什么重要？

## 深挖与误区

- 不要只讲“runtime 负责调度”，要讲调度什么、为什么难
- 不要只讲吞吐，不讲 TTFT、TPOT 和 P99
- 不要把 serving 问题回答成纯编译优化问题
