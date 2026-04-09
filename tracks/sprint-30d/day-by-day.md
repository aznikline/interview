# 30 天逐日执行表

这个版本不是单纯的阅读清单，而是 `每天看什么 + 每天练什么 + 每天至少输出什么`。

## Week 1：后端主链路

### Day 1

- 看：[02-mysql-transactions-and-locks.md](/Users/wizout/op/interview/docs/topics/backend/02-mysql-transactions-and-locks.md)
- 练：[questions/backend/high-frequency.md](/Users/wizout/op/interview/questions/backend/high-frequency.md)
- 输出：口述 `B+ 树、MVCC、索引失效` 这 3 题

### Day 2

- 看：[03-redis-and-cache-consistency.md](/Users/wizout/op/interview/docs/topics/backend/03-redis-and-cache-consistency.md)
- 练：[questions/backend/distributed-and-db.md](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- 输出：口述 `缓存一致性、缓存击穿、热 key`

### Day 3

- 看：[04-mq-reliability-and-idempotency.md](/Users/wizout/op/interview/docs/topics/backend/04-mq-reliability-and-idempotency.md)
- 练：补你自己的项目例子
- 输出：口述 `消息不丢、重复消费、幂等`

### Day 4

- 看：[01-os-core.md](/Users/wizout/op/interview/docs/topics/operating-system/01-os-core.md)
- 练：[questions/operating-system/high-frequency.md](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
- 输出：口述 `进程 vs 线程、上下文切换、用户态 vs 内核态`

### Day 5

- 看：[02-memory-and-io.md](/Users/wizout/op/interview/docs/topics/operating-system/02-memory-and-io.md)
- 练：[questions/operating-system/concurrency-and-memory.md](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)
- 输出：口述 `虚拟内存、缺页、中断、零拷贝`

### Day 6

- 做：[backend-general.md](/Users/wizout/op/interview/practice/mock-interviews/backend-general.md)
- 输出：完整 mock 一次，按 [scorecard.md](/Users/wizout/op/interview/practice/mock-interviews/scorecard.md) 打分

### Day 7

- 做周复盘
- 输出：列出后端和 OS 各自最弱的 `3` 个点

## Week 2：算法和系统设计方法

### Day 8

- 看：[01-algorithm-methodology.md](/Users/wizout/op/interview/docs/topics/algorithm/01-algorithm-methodology.md)
- 输出：总结你最容易失手的 `2` 类题型

### Day 9

- 看：[02-common-patterns.md](/Users/wizout/op/interview/docs/topics/algorithm/02-common-patterns.md)
- 练：[questions/algorithm/high-frequency.md](/Users/wizout/op/interview/questions/algorithm/high-frequency.md)
- 输出：口述 `滑动窗口、双指针、二叉树遍历`

### Day 10

- 看：[03-frameworks-and-drills.md](/Users/wizout/op/interview/docs/topics/algorithm/03-frameworks-and-drills.md)
- 练：[questions/algorithm/patterns-and-dp.md](/Users/wizout/op/interview/questions/algorithm/patterns-and-dp.md)
- 输出：口述 `DP 状态定义 + 转移方程`

### Day 11

- 看：[01-system-design-methodology.md](/Users/wizout/op/interview/docs/topics/system-design/01-system-design-methodology.md)
- 补：[系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
- 输出：用 2 分钟讲一遍系统设计答题框架

### Day 12

- 看：[02-cache-consistency-and-traffic.md](/Users/wizout/op/interview/docs/topics/system-design/02-cache-consistency-and-traffic.md)
- 输出：口述 `缓存、一致性、异步化` 的 trade-off

### Day 13

- 看：[03-seckill-and-high-concurrency.md](/Users/wizout/op/interview/docs/topics/system-design/03-seckill-and-high-concurrency.md)
- 输出：完整讲一遍秒杀链路

### Day 14

- 练：[questions/system-design/high-frequency.md](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
- 输出：完成 `1` 道系统设计题的完整口述

## Week 3：案例和项目表达

### Day 15

- 练：[questions/system-design/design-cases.md](/Users/wizout/op/interview/questions/system-design/design-cases.md)
- 输出：补一版你自己的系统设计模板

### Day 16

- 看：[url-shortener.md](/Users/wizout/op/interview/projects/backend-case-studies/url-shortener.md)
- 输出：总结短链接题的容量估算和冲突点

### Day 17

- 看：[feed-system.md](/Users/wizout/op/interview/projects/design-case-studies/feed-system.md)
- 输出：总结 pull / push / hybrid 的取舍

### Day 18

- 看：[seckill-system.md](/Users/wizout/op/interview/projects/design-case-studies/seckill-system.md)
- 输出：总结秒杀题里的削峰、限流、库存一致性

### Day 19

- 做模拟面试
- 输出：录一段 `5-8` 分钟的系统设计口述

### Day 20

- 做周复盘
- 输出：列出你最不稳的 `3` 道系统设计题

## Week 4：AI 编译器和综合收口

### Day 21

- 看：[01-ai-compiler-core.md](/Users/wizout/op/interview/docs/topics/ai-compiler/01-ai-compiler-core.md)
- 输出：讲清完整链路

### Day 22

- 看：[02-ir-lowering-and-dialects.md](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
- 输出：口述 `IR、dialect、lowering`

### Day 23

- 看：[03-kernel-fusion-and-runtime.md](/Users/wizout/op/interview/docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
- 输出：口述 `fusion、layout、runtime`

### Day 24

- 看：[04-getting-started-and-chapters.md](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
- 练：[questions/ai-compiler/high-frequency.md](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
- 输出：完成 `5` 个 AI 编译器 1 分钟回答

### Day 25

- 看：[AI 编译器答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-ai-compiler-interview.md)
- 练：[questions/ai-compiler/deep-dive.md](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- 输出：把一个优化案例按 `五层答法` 讲出来

### Day 26

- 做：[ai-infra.md](/Users/wizout/op/interview/practice/mock-interviews/ai-infra.md)
- 输出：完成一轮 AI Infra mock

### Day 27

- 做：[senior-backend.md](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)
- 输出：完成一轮后端 mock

### Day 28

- 做：[ai-compiler-deep-dive.md](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)
- 输出：完成一轮 AI 编译器深挖 mock

### Day 29

- 综合查漏补缺
- 输出：每个领域补 `3` 个最弱点

### Day 30

- 全真模拟
- 输出：按 [scorecard.md](/Users/wizout/op/interview/practice/mock-interviews/scorecard.md) 做总评
