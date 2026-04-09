# AI 编译器专题首页

## 1 分钟速答

AI 编译器方向的关键不是框架名，而是你是否理解 `IR`、`lowering`、`fusion`、`layout`、`kernel`、`runtime` 和 `hardware` 之间的关系，并能用性能指标解释优化收益。

## 核心机制

### 推荐学习顺序

1. AI 编译器整体链路
2. 多级 IR 与 lowering
3. kernel 融合与 runtime 协同
4. 结合 LLM 推理和 runtime 场景讲项目表达

### 必读文档

- [01-ai-compiler-core.md](/Users/wizout/op/interview/docs/topics/ai-compiler/01-ai-compiler-core.md)
- [02-ir-lowering-and-dialects.md](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
- [03-kernel-fusion-and-runtime.md](/Users/wizout/op/interview/docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)

## 高频问法

- MLIR、XLA、TVM、Triton 分别解决什么问题？
- 动态 shape 为什么难？
- layout 为什么重要？
- 编译器和 runtime 怎么分工？

## 深挖与误区

- 不要只背框架名
- 不要只讲 compiler，不讲 runtime
- 必须能说出指标：TTFT、TPOT、throughput、显存占用、P99

## 下一步

- 刷 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- 看 [项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)

