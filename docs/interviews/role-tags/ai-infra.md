# 角色标签：AI Infra

## 适合谁

- 目标岗位是 AI Infra、推理优化、训练平台、模型加速、系统工程
- 日常工作会落在 CUDA、通信、训练并行、Serving、推理链路
- 面试里通常同时考后端、OS、系统设计和 GPU / 分布式 / 推理系统工程

## 核心能力画像

- 后端与系统基础扎实
- 操作系统和性能分析有抓手
- 对 CUDA、通信、训练并行、Serving、硬件协同有整体理解
- 能用指标说性能优化，不只会背框架名

## 推荐入口

- [AI Infra 专题首页](/Users/wizout/op/interview/docs/topics/ai-infra/00-index.md)
- [AI Infra 核心题清单](/Users/wizout/op/interview/questions/ai-infra/00-must-know.md)
- [AI Infra 代表题清单](/Users/wizout/op/interview/questions/ai-infra/representative-scenarios.md)
- [AI Infra 21 天计划](/Users/wizout/op/interview/tracks/ai-infra-21d/README.md)
- [AI Infra 压测包](/Users/wizout/op/interview/practice/drills/ai-infra-pressure-pack.md)

## 正确起手顺序

1. 先保住 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md) 里和性能现象最相关的题
2. 再过 [AI Infra 核心题清单](/Users/wizout/op/interview/questions/ai-infra/00-must-know.md)
3. 再补 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md) 里容量、限流、恢复这些 Serving 相关问题
4. 跑 [AI Infra 21 天计划](/Users/wizout/op/interview/tracks/ai-infra-21d/README.md)
5. 最后跑 [AI Infra 压测包](/Users/wizout/op/interview/practice/drills/ai-infra-pressure-pack.md) 和 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 必须先保住的题

- warp 是什么？
- occupancy 高是不是一定更快？
- 为什么通信会成为多卡训练瓶颈？
- 显存优化常见手段有哪些？
- 为什么 decode 常 memory bound？
- 怎么用 TTFT、吞吐、P99 和显存讲 trade-off？

## 常见短板

- 只会背 CUDA / NCCL 术语
- 不会把 GPU、通信、训练、Serving 串成一条链路
- 不会用吞吐、P99、显存和带宽讲优化收益
