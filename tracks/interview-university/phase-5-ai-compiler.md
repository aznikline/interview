# Phase 5: AI Compiler And AI Infra

这个阶段是差异化模块。它不是用来掩盖主线短板的，而是给你在 AI Infra / 推理优化 / 编译器方向上建立更高上限。

## 阶段目标

- 讲清 AI 编译器的完整链路
- 区分 compiler 和 runtime 的边界
- 用指标解释优化收益
- 把一个真实优化案例讲成完整故事

## 建议时长

- 标准版：`7-10 天`
- 压缩版：`3-5 天`

## 推荐学习顺序

1. [AI 编译器专题首页](../../docs/topics/ai-compiler/00-index.md)
2. [AI 编译器整体链路](../../docs/topics/ai-compiler/01-ai-compiler-core.md)
3. [IR、lowering 与 dialect](../../docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
4. [kernel、fusion 与 runtime](../../docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
5. [入门与章节推进](../../docs/topics/ai-compiler/04-getting-started-and-chapters.md)
6. [AI 编译器答题法](../../docs/guides/how-to-approach-ai-compiler-interview.md)
7. [AI 编译器核心题清单](../../questions/ai-compiler/00-must-know.md)
8. [AI 编译器高频题](../../questions/ai-compiler/high-frequency.md)
9. [AI 编译器深挖题](../../questions/ai-compiler/deep-dive.md)
10. [LLM 推理编译案例](../../projects/ai-compiler-case-studies/llm-inference-compiler.md)
11. [runtime 调度案例](../../projects/ai-compiler-case-studies/runtime-scheduling.md)
12. [项目表达稿](../../projects/ai-compiler-case-studies/project-storytelling.md)

## 这阶段必须拿下的核心问题

- 为什么需要多级 IR？
- lowering 的本质是什么？
- fusion 为什么可能提速，也可能拖慢？
- layout 为什么影响性能？
- compiler 和 runtime 如何分工？
- TTFT、TPOT、throughput 分别代表什么？

## 每周输出要求

### 输出 1：链路口述

至少完成一次 `模型/图 -> IR -> lowering -> fusion -> kernel -> runtime -> 指标` 的完整口述。

### 输出 2：优化案例

选一个你熟悉的优化点，按下面结构讲清：

- 瓶颈是什么
- 为什么定位到这里
- 为什么选这个优化
- 指标改善了什么
- 边界和代价是什么

### 输出 3：mock

至少完成一次 [ai-infra.md](../../practice/mock-interviews/ai-infra.md) 或 [ai-compiler-deep-dive.md](../../practice/mock-interviews/ai-compiler-deep-dive.md)。

## 退出条件

- 不再把 AI 编译器准备成框架名背诵
- 能稳定回答 `IR / lowering / fusion / runtime / 指标` 五大类问题
- 至少有 `1` 个可讲的 AI Infra / 编译器优化故事

## 这个阶段最容易失败的方式

- 只讲 compiler，不讲 runtime
- 只讲概念，不讲指标
- 只讲框架名，不讲链路
- 说做过优化，但说不出瓶颈和收益
