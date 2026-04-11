# AI Infra 专题首页

## 1 分钟速答

AI Infra 面试不等于 LLM 八股，也不等于 AI 编译器。它更像一条从硬件到系统的工程链路：`CUDA / GPU 基础 -> 通信与互联 -> 训练并行 -> 推理系统 -> Serving 指标 -> 工具链与排障`。你要能讲的不只是模型，而是模型为什么在这台机器、这套网络、这条服务链路上跑成现在这个样子。

## 核心机制

### 推荐学习顺序

1. GPU / CUDA 基础
2. 通信与互联
3. 训练并行与显存优化
4. 推理与 Serving
5. 工具链、框架实现与项目实践

### 必读文档

- [01-cuda-and-gpu-basics.md](01-cuda-and-gpu-basics.md)
- [02-communication-and-parallelism.md](02-communication-and-parallelism.md)
- [03-training-and-serving-systems.md](03-training-and-serving-systems.md)
- [04-local-source-map.md](04-local-source-map.md)

### 学完后应该具备什么能力

- 能解释 warp、occupancy、shared memory、memory coalescing 这些 CUDA 核心概念
- 能讲清 NCCL、拓扑、带宽、通信开销和训练并行之间的关系
- 能把训练 / 推理 / Serving / 调度 / 恢复讲成一条系统工程链路
- 能把 `ai-infra-hpc` 和 `OriginDL` 这些本地参考仓库映射到自己的学习路径

## 高频问法

- CUDA kernel 为什么会慢？
- occupancy 高是不是一定更快？
- 通信为什么会成为多卡训练瓶颈？
- 显存优化有哪些常见手段？
- TTFT、吞吐和显存为什么经常互相牵制？

## 深挖与误区

- 不要只背 CUDA 术语，不会讲访存和调度
- 不要把训练并行只讲成名词罗列
- 不要把 AI Infra 讲成“比 AI 编译器更偏工程”这种空话

## 下一步

- 刷 [AI Infra 核心题清单](../../../questions/ai-infra/00-must-know.md)
- 刷 [AI Infra 代表题清单](../../../questions/ai-infra/representative-scenarios.md)
- 跑 [AI Infra 21 天计划](../../../tracks/ai-infra-21d/README.md)
- 跑 [AI Infra 压测包](../../../practice/drills/ai-infra-pressure-pack.md)
