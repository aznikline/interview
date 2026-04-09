# Interview University 学习计划

这份文档是整个仓库的主入口，结构明确参考 `coding-interview-university`。

使用方式很简单：按顺序推进，完成一项就打勾，不要跳跃式学习。

## 建议时长

- `6-8 周`：比较完整地走完一轮
- `4 周`：压缩版，保主线
- `1 周`：只做救火和最终复习

如果你时间不足，优先保证：

1. 后端主链路
2. 算法高频模式
3. OS 与并发
4. 系统设计答题框架
5. 项目表达

AI 编译器是差异化模块，不是拿来替代主线短板的。

## Before You Start

- [ ] 明确你的目标岗位：通用后端 / 基础架构 / AI Infra / AI 编译器
- [ ] 明确你的主语言：`Java / Go / C++ / Python` 选一个作为面试主语言
- [ ] 明确你的时间预算：`1 周 / 1 个月 / 2 个月+`
- [ ] 建立一个弱项清单，后面每周更新一次
- [ ] 阅读 [总路线图](/Users/wizout/op/interview/docs/roadmap/00-overview.md)

## How to Study

- [ ] 每天学习一个主题，不要同一天到处跳
- [ ] 每学完一个主题，至少完成一次口述输出
- [ ] 每周至少做一次 mock
- [ ] 每周至少做一次复盘
- [ ] 只背知识点不够，必须把知识点连到问题、系统、项目、指标

### 每个阶段的最低交付

- [ ] 至少完成 `1` 份阶段性弱项清单
- [ ] 至少完成 `1` 次 mock 或口述录音
- [ ] 至少完成 `1` 份项目/案例复盘

### 进入下一阶段的标准

- [ ] 不是“看完了”，而是“能讲出来”
- [ ] 每个阶段至少能稳定讲 `5-10` 个高频问题
- [ ] 对该阶段至少有 `1` 次输出记录，而不是只读材料

## Phase 1: Backend Core

目标：把后端主链路讲顺。

建议时长：`10-14 天`

阶段指南：

- [Phase 1: Backend Core](/Users/wizout/op/interview/tracks/interview-university/phase-1-backend-core.md)

- [ ] 阅读 [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
- [ ] 阅读 [后端基础总览](/Users/wizout/op/interview/docs/topics/backend/01-backend-fundamentals.md)
- [ ] 阅读 [MySQL 事务、锁与 MVCC](/Users/wizout/op/interview/docs/topics/backend/02-mysql-transactions-and-locks.md)
- [ ] 阅读 [Redis 与缓存一致性](/Users/wizout/op/interview/docs/topics/backend/03-redis-and-cache-consistency.md)
- [ ] 阅读 [MQ 可靠性与幂等](/Users/wizout/op/interview/docs/topics/backend/04-mq-reliability-and-idempotency.md)
- [ ] 刷 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- [ ] 刷 [后端高频题](/Users/wizout/op/interview/questions/backend/high-frequency.md)
- [ ] 刷 [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- [ ] 完成一次 [后端基础 Mock](/Users/wizout/op/interview/practice/mock-interviews/backend-general.md)

阶段验收：

- [ ] 能讲 `MySQL -> Redis -> MQ -> 一致性 -> 高并发` 的完整链路
- [ ] 能从你的项目里举出一个真实工程案例
- [ ] 能在追问下继续讲锁、日志、幂等、热 key、消息积压

## Phase 2: Algorithms and Data Structures

目标：把算法从“会做”推进到“会讲”。

建议时长：`10-14 天`

阶段指南：

- [Phase 2: Algorithms And Data Structures](/Users/wizout/op/interview/tracks/interview-university/phase-2-algorithms.md)

- [ ] 阅读 [算法专题首页](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
- [ ] 阅读 [算法方法论](/Users/wizout/op/interview/docs/topics/algorithm/01-algorithm-methodology.md)
- [ ] 阅读 [高频模式](/Users/wizout/op/interview/docs/topics/algorithm/02-common-patterns.md)
- [ ] 阅读 [框架、例题和训练法](/Users/wizout/op/interview/docs/topics/algorithm/03-frameworks-and-drills.md)
- [ ] 刷 [算法核心题清单](/Users/wizout/op/interview/questions/algorithm/00-must-know.md)
- [ ] 刷 [算法高频题](/Users/wizout/op/interview/questions/algorithm/high-frequency.md)
- [ ] 刷 [模式与 DP](/Users/wizout/op/interview/questions/algorithm/patterns-and-dp.md)
- [ ] 执行 [每日 Drill](/Users/wizout/op/interview/practice/drills/daily-drill.md)

阶段验收：

- [ ] 能口述滑动窗口、双指针、二叉树、回溯、DP 的核心模板
- [ ] 能在写代码前先说出思路、复杂度和边界条件
- [ ] 能稳定完成中等难度题的白板表达

## Phase 3: Operating Systems and Concurrency

目标：把 OS 和并发问题讲成工程语境里的答案，而不是课本摘录。

建议时长：`7-10 天`

阶段指南：

- [Phase 3: Operating Systems And Concurrency](/Users/wizout/op/interview/tracks/interview-university/phase-3-operating-systems.md)

- [ ] 阅读 [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
- [ ] 阅读 [OS 核心](/Users/wizout/op/interview/docs/topics/operating-system/01-os-core.md)
- [ ] 阅读 [内存与 I/O](/Users/wizout/op/interview/docs/topics/operating-system/02-memory-and-io.md)
- [ ] 阅读 [并发与调度](/Users/wizout/op/interview/docs/topics/operating-system/03-concurrency-and-scheduling.md)
- [ ] 刷 [OS 核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- [ ] 刷 [OS 高频题](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
- [ ] 刷 [并发与内存题](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)

阶段验收：

- [ ] 能解释进程、线程、虚拟内存、缺页、中断、零拷贝、锁与调度
- [ ] 能把 OS 问题连到服务稳定性和性能瓶颈
- [ ] 能回答“为什么这个机制会导致性能问题”

## Phase 4: System Design and Distributed Trade-offs

目标：建立“拆题 -> 估算 -> 架构 -> trade-off -> 故障处理”的答题框架。

建议时长：`10-14 天`

阶段指南：

- [Phase 4: System Design And Distributed Trade-offs](/Users/wizout/op/interview/tracks/interview-university/phase-4-system-design.md)

- [ ] 阅读 [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
- [ ] 阅读 [系统设计方法论](/Users/wizout/op/interview/docs/topics/system-design/01-system-design-methodology.md)
- [ ] 阅读 [缓存一致性与流量治理](/Users/wizout/op/interview/docs/topics/system-design/02-cache-consistency-and-traffic.md)
- [ ] 阅读 [秒杀与高并发](/Users/wizout/op/interview/docs/topics/system-design/03-seckill-and-high-concurrency.md)
- [ ] 阅读 [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
- [ ] 刷 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
- [ ] 刷 [系统设计高频题](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
- [ ] 刷 [系统设计案例题](/Users/wizout/op/interview/questions/system-design/design-cases.md)
- [ ] 阅读 [短链接案例](/Users/wizout/op/interview/projects/backend-case-studies/url-shortener.md)
- [ ] 阅读 [Feed 系统案例](/Users/wizout/op/interview/projects/design-case-studies/feed-system.md)
- [ ] 阅读 [秒杀系统案例](/Users/wizout/op/interview/projects/design-case-studies/seckill-system.md)

阶段验收：

- [ ] 能完整讲 2 道系统设计题
- [ ] 每道题都能覆盖需求、估算、链路、瓶颈、trade-off、故障处理
- [ ] 不会一上来就堆 Redis / MQ / 分库分表

## Phase 5: AI Compiler and AI Infra

目标：建立差异化专题，不把 AI 编译器准备成术语背诵。

建议时长：`7-10 天`

阶段指南：

- [Phase 5: AI Compiler And AI Infra](/Users/wizout/op/interview/tracks/interview-university/phase-5-ai-compiler.md)

- [ ] 阅读 [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [ ] 阅读 [AI 编译器整体链路](/Users/wizout/op/interview/docs/topics/ai-compiler/01-ai-compiler-core.md)
- [ ] 阅读 [IR、lowering 与 dialect](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
- [ ] 阅读 [kernel、fusion 与 runtime](/Users/wizout/op/interview/docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
- [ ] 阅读 [入门与章节推进](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
- [ ] 阅读 [AI 编译器答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-ai-compiler-interview.md)
- [ ] 刷 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- [ ] 刷 [AI 编译器高频题](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
- [ ] 刷 [AI 编译器深挖题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- [ ] 阅读 [LLM 推理编译案例](/Users/wizout/op/interview/projects/ai-compiler-case-studies/llm-inference-compiler.md)
- [ ] 阅读 [runtime 调度案例](/Users/wizout/op/interview/projects/ai-compiler-case-studies/runtime-scheduling.md)
- [ ] 阅读 [项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)
- [ ] 完成一次 [AI Infra Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-infra.md)
- [ ] 完成一次 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)

阶段验收：

- [ ] 能讲清 `模型/图 -> IR -> lowering -> fusion -> kernel -> runtime -> 指标`
- [ ] 能把一个优化案例讲成“瓶颈、方案、收益、边界”
- [ ] 能解释为什么这个模块该放在 compiler 或 runtime

## Phase 6: Final Review

目标：把知识从“知道”压到“能过面试”。

建议时长：`5-7 天`

- [ ] 执行 [Final Review Checklist](/Users/wizout/op/interview/tracks/interview-university/final-review.md)
- [ ] 完成一次 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)
- [ ] 回看 [review-checklists.md](/Users/wizout/op/interview/docs/guides/review-checklists.md)
- [ ] 回看 [answer-methodology.md](/Users/wizout/op/interview/docs/guides/answer-methodology.md)
- [ ] 更新一版你自己的项目表达稿

阶段验收：

- [ ] 你能稳定完成 3 轮不同方向的 mock
- [ ] 你有一份明确的弱项清单和冲刺清单
- [ ] 你能在高压状态下维持答题结构

## If You Only Have 1 Month

- [ ] 执行 [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)

## If You Only Have 1 Week

- [ ] 执行 [7 天急救计划](/Users/wizout/op/interview/practice/drills/7-day-rescue-plan.md)

## Optional Topics

- [ ] 阅读 [Optional Topics](/Users/wizout/op/interview/tracks/interview-university/optional-topics.md)

## Once You're Closer To The Interview

- [ ] 阅读 [Closer To The Interview](/Users/wizout/op/interview/tracks/interview-university/closer-to-interview.md)
- [ ] 只围绕弱项清单和 mock 结果做最后修补
