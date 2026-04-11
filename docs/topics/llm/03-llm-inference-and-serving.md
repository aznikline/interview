# LLM 推理与 Serving

## 1 分钟速答

推理面试的核心不是说出 vLLM、TGI、TensorRT-LLM 这些名字，而是讲清：为什么推理慢、KV Cache 在解决什么、TTFT/TPOT/吞吐怎么取舍、batching 和调度为什么会牵动整条服务链路。

## 核心机制

### 推理高频点

- prefill / decode 两阶段
- KV Cache 的命中与显存占用
- 动态 batching、连续 batching、admission control
- 模型并行、量化、kernel 优化

### 服务高频点

- TTFT、TPOT、throughput、P99 latency
- prompt 长度、batch size、并发数、显存的 trade-off
- cache、限流、降级、恢复

### 工程实践高频点

- vLLM、TGI、TensorRT-LLM 的定位
- 为什么 decode 常常 memory bound
- 为什么平均更快不代表线上更稳

## 高频问法

- KV Cache 为什么重要？
- TTFT 和 TPOT 分别代表什么？
- 为什么 dynamic batching 很有用但也很危险？
- vLLM 在解决哪类问题？

## 深挖与误区

- 不要只报框架名，不讲它在链路里的角色
- 不要只看平均耗时，不看 P99 和稳定性
- 不要把推理优化讲成单点技巧，忽略调度和服务侧约束
