# 项目案例：LLM 推理编译优化

## 场景

面试中经常会被问：你如何理解大模型推理优化链路？可以用这份案例组织回答。

## 核心链路

1. 模型图导出与 IR 表达
2. 图级优化：常量折叠、融合、layout 传播
3. kernel 选择或生成
4. runtime 调度：batching、memory planning、stream
5. 设备执行与性能分析

## 可讲的优化点

- fused attention / RMSNorm / matmul kernel
- KV cache 布局优化
- prefill 与 decode 分阶段优化
- 动态 batch 与吞吐 / 延迟平衡

## 面试表达重点

- 先说瓶颈在哪：memory bound 还是 compute bound
- 再说优化抓手在哪
- 最后说如何验证：tokens/s、TTFT、TPOT、显存占用

