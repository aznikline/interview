# 角色标签：AI Infra / AI 编译器

## 适合谁

- 目标岗位是 AI Infra、推理优化、模型加速、编译器工程
- 日常工作会落在服务性能、runtime、kernel、图编译或推理链路
- 面试里通常同时考后端、OS、系统设计和 AI 编译器差异化内容

## 核心能力画像

- 后端与系统基础扎实
- 操作系统和性能分析有抓手
- 对图编译、kernel、runtime、硬件协同有整体理解
- 能用指标说性能优化，不只会背框架名

## 推荐入口

- [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
- [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)

## 正确起手顺序

1. 先保住 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md) 里和性能现象最相关的题
2. 再过 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
3. 再补 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md) 里容量、限流、恢复这些 runtime 相关问题
4. 跑 [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
5. 最后做 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md) 和 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 必须先保住的题

- 为什么要多级 IR？
- lowering 在做什么？
- 算子融合为什么可能更快，也可能更慢？
- runtime 为什么不能完全替代编译优化？
- decode 为什么常 memory bound？
- 怎么用 TTFT、TPOT、吞吐和显存讲优化收益？

## 常见短板

- 只会背 MLIR、XLA、TVM、Triton 名字，不会讲层级边界
- 不会把 compiler pass、kernel 和 runtime 连起来
- 不会用 TTFT、TPOT、吞吐、显存占用这些指标讲优化收益
