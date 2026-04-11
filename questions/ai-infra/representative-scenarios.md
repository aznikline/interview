# AI Infra 代表题清单

## 题目

如果只保最值得讲的一批 AI Infra 题，应该怎么选？

## 一句话回答

先保 `CUDA 基础 / 通信并行 / 训练系统 / 推理 Serving / 框架实现` 五类场景的代表题。不是把硬件名词全背下来，而是每道题都能讲到性能瓶颈和工程取舍。

## 展开回答

| 场景 | 推荐代表题 | 你要练什么 |
| --- | --- | --- |
| CUDA 基础 | warp、occupancy、shared memory、coalescing | GPU 执行和访存本质 |
| 通信并行 | AllReduce、数据并行、张量并行、流水线并行 | 计算和通信 trade-off |
| 训练系统 | mixed precision、checkpointing、显存优化 | 显存和吞吐平衡 |
| 推理 Serving | KV Cache、TTFT/TPOT、dynamic batching | 延迟与吞吐平衡 |
| 框架实现 | 自动微分、算子、训练链路、推理链路 | 从零实现框架的工程视角 |

## 面试官追问

- 为什么 occupancy 不是银弹？
- 为什么通信拓扑会直接影响性能？
- 为什么框架实现题能拉开差距？

## 关联知识点

- [AI Infra 核心题清单](00-must-know.md)
- [AI Infra 高频题](high-frequency.md)
- [AI Infra 专题首页](../../docs/topics/ai-infra/00-index.md)
