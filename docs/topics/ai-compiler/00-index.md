# AI 编译器专题首页

## 1 分钟速答

AI 编译器方向的关键不是框架名，而是你是否理解 `IR`、`lowering`、`fusion`、`layout`、`kernel`、`runtime` 和 `hardware` 之间的关系，并能用性能指标解释优化收益。

## 核心机制

### 推荐学习顺序

1. AI 编译器整体链路
2. 多级 IR 与 lowering
3. kernel 融合与 runtime 协同
4. 入门章节化学习
5. 项目表达与 mock

### 必读文档

- [01-ai-compiler-core.md](/Users/wizout/op/interview/docs/topics/ai-compiler/01-ai-compiler-core.md)
- [02-ir-lowering-and-dialects.md](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
- [03-kernel-fusion-and-runtime.md](/Users/wizout/op/interview/docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
- [04-getting-started-and-chapters.md](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
- [AI 编译器答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-ai-compiler-interview.md)

### 学完这一组内容后应该具备什么能力

- 能讲完整条 AI 编译器链路
- 能区分 compiler 和 runtime 的边界
- 能把优化收益落到 TTFT、TPOT、throughput、显存占用等指标

## 高频问法

- MLIR、XLA、TVM、Triton 分别解决什么问题？
- 为什么要多级 IR？
- 动态 shape 为什么难？
- layout 为什么影响性能？
- 编译器和 runtime 怎么分工？

## 深挖与误区

- 不要只背框架名
- 不要只讲 compiler，不讲 runtime
- 不要只讲概念，不讲指标

## 下一步

- 刷 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- 看 [项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)
