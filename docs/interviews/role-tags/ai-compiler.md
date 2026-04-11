# 角色标签：AI 编译器

## 适合谁

- 目标岗位是 AI 编译器、图编译、kernel 优化、代码生成
- 工作重点更偏 IR、pass pipeline、fusion、layout、codegen
- 面试里仍会考 runtime 和推理服务，但主战场是编译链路本身

## 核心能力画像

- IR 分层和 lowering
- fusion、layout、kernel 与硬件映射
- compile time 和 runtime 的边界
- 性能指标和 workload 分析
- 能把优化讲成 `瓶颈 -> 动作 -> 指标 -> 边界`

## 推荐入口

- [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
- [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)

## 正确起手顺序

1. 先保住 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
2. 再补 [编译原理基础、SSA 与数据流](/Users/wizout/op/interview/docs/topics/ai-compiler/06-compiler-fundamentals-and-ssa.md)
3. 再看 [IR、Lowering 与 Dialect](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md) 和 [Serving Runtime 与在线调度](/Users/wizout/op/interview/docs/topics/ai-compiler/05-serving-and-runtime-systems.md)
4. 跑 [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
5. 做 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md) 和 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 必须先保住的题

- 为什么要多级 IR？
- lowering 到底在做什么？
- fusion 和 layout 为什么会影响性能？
- compile time 和 runtime 的边界怎么划？
- dynamic shape 为什么难？
- 怎么判断一个优化值得上线？

## 常见失分点

- 只会背框架和术语，不会说抽象层次
- 不会把 pass、kernel、runtime 连到同一条链路
- 只讲平均性能，不讲 P99、TTFT、TPOT 或显存代价
