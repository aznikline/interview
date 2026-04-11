# AI Infra 核心题清单

## 题目

AI Infra 面试最应该优先准备哪些题，顺序应该怎么排？

## 一句话回答

先保 `CUDA / GPU 基础 -> 通信与并行 -> 训练系统 -> 推理 Serving -> 项目实践` 这条链路。顺序上先保住硬件和系统概念，再补工程链路和指标 trade-off。

## 展开回答

### 第一层：必须先拿下的 10 题

- warp 是什么？
- occupancy 高是不是一定更快？
- shared memory 为什么有用也有坑？
- memory coalescing 为什么重要？
- 为什么多卡训练会被通信拖慢？
- 数据并行、张量并行、流水线并行怎么选？
- 显存优化有哪些常见手段？
- 为什么 decode 常 memory bound？
- TTFT、吞吐、P99 之间怎么取舍？
- 恢复阶段为什么也会再次打崩推理服务？

### 1 分钟速答表

| 题目 | 最低合格回答 |
| --- | --- |
| warp 是什么？ | warp 是 GPU 执行调度的基本单位，通常一组线程以 SIMT 方式一起执行。 |
| occupancy 高是不是一定更快？ | 不是，高 occupancy 只说明驻留线程多，真正性能还看访存、分支和寄存器压力。 |
| 通信为什么会成为多卡训练瓶颈？ | 因为计算能并行，但参数和梯度同步要吃带宽、拓扑和调度成本。 |
| decode 为什么常 memory bound？ | 因为每步计算量相对小，但 KV Cache 读取和内存带宽压力很高。 |
| 显存优化有哪些常见手段？ | mixed precision、checkpointing、参数切分、激活重算、量化等。 |

## 面试官追问

- occupancy 和 latency hiding 是什么关系？
- 为什么加卡不等于线性提速？
- 推理服务为什么恢复后也会抖？

## 易错点

- 只会背 CUDA 术语
- 只会报并行名词
- 不会讲指标和系统后果

## 关联知识点

- [AI Infra 专题首页](/Users/wizout/op/interview/docs/topics/ai-infra/00-index.md)
- [AI Infra 高频题](/Users/wizout/op/interview/questions/ai-infra/high-frequency.md)
- [AI Infra 代表题清单](/Users/wizout/op/interview/questions/ai-infra/representative-scenarios.md)
- [AI Infra 21 天计划](/Users/wizout/op/interview/tracks/ai-infra-21d/README.md)
- [AI Infra 压测包](/Users/wizout/op/interview/practice/drills/ai-infra-pressure-pack.md)
