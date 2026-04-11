# AI Compiler Week Plan

适用场景：

- 你要在一周内快速建立 AI 编译器专题的面试表达
- 你目标岗位偏 AI Infra / 推理优化 / 编译器工程

## Day 1：整体链路

- 阅读 [01-ai-compiler-core.md](../../docs/topics/ai-compiler/01-ai-compiler-core.md)
- 输出：讲一遍 `模型/图 -> IR -> lowering -> fusion -> kernel -> runtime -> 指标`

## Day 2：IR 与 lowering

- 阅读 [02-ir-lowering-and-dialects.md](../../docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
- 输出：讲清多级 IR、dialect、lowering

## Day 3：fusion、layout、kernel

- 阅读 [03-kernel-fusion-and-runtime.md](../../docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
- 输出：回答
  - 为什么 fusion 能提速
  - 为什么可能变慢
  - layout 为什么影响性能

## Day 4：runtime 与 serving

- 阅读 [runtime-scheduling.md](../../projects/ai-compiler-case-studies/runtime-scheduling.md)
- 输出：讲清 dynamic batching、KV cache、runtime 调度

## Day 5：高频题

- 刷 [AI 编译器核心题清单](../../questions/ai-compiler/00-must-know.md)
- 刷 [AI 编译器高频题](../../questions/ai-compiler/high-frequency.md)
- 输出：完成 `5` 个 1 分钟回答

## Day 6：项目表达

- 阅读 [project-storytelling.md](../../projects/ai-compiler-case-studies/project-storytelling.md)
- 输出：写一版你自己的优化故事

## Day 7：Mock 与复盘

- 做 [ai-infra.md](../../practice/mock-interviews/ai-infra.md) 或 [ai-compiler-deep-dive.md](../../practice/mock-interviews/ai-compiler-deep-dive.md)
- 用 [scorecard.md](../../practice/mock-interviews/scorecard.md) 打分
- 输出：最薄弱的 `5` 个点
