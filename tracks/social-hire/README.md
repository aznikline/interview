# 社招路线

适合：

- `3-8` 年后端 / 平台 / 基础架构工程师
- 已经做过真实业务，但知识体系和面试表达不稳定
- 面试重点更偏项目、稳定性、系统设计和 trade-off

## 核心特点

- 系统设计、项目表达和稳定性治理比校招更重要
- 面试官会更关注真实业务场景中的 `约束 / 代价 / 故障 / 复盘`
- 算法通常不是唯一主战场，但不能完全失分

## 优先顺序

项目表达 > 后端八股 > 系统设计 > 操作系统与性能 > 算法

## 4 周起手计划

### Week 1：后端主链路收口

- 看 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- 看 [后端场景地图](/Users/wizout/op/interview/docs/topics/backend/08-backend-scenario-map.md)
- 跑 [后端场景 14 天计划](/Users/wizout/op/interview/tracks/backend-scenario-14d/README.md)
- 看 [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- 跑 [后端与系统设计口述速答包](/Users/wizout/op/interview/practice/drills/backend-and-system-design-oral-pack.md)

最低输出：

- 能稳定讲 `MySQL / Redis / MQ / 一致性` 四组题
- 能讲一个你做过的核心项目主链路

### Week 2：系统设计与可靠性

- 看 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
- 看 [系统设计进阶题](/Users/wizout/op/interview/questions/system-design/design-cases.md)
- 跑 [可靠性与高并发深水区 Drill](/Users/wizout/op/interview/practice/drills/reliability-deep-dive.md)

最低输出：

- 至少完整口述 `2` 道设计题
- 能讲恢复期、限流、降级、补偿

### Week 3：OS、性能与项目表达

- 看 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- 看 [Linux 可观测性与性能排障](/Users/wizout/op/interview/docs/topics/operating-system/04-linux-observability-and-tuning.md)
- 修 [项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md) 的结构，哪怕你讲的是后端项目

最低输出：

- 能解释 `epoll / 上下文切换 / 锁竞争 / page fault` 和真实服务问题的关系
- 能把项目压成 `背景 -> 瓶颈 -> 方案 -> 指标 -> 复盘`

### Week 4：Mock 与追问承压

- 做 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)
- 做 [可靠性与基础架构深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/reliability-and-infra.md)
- 跑 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

最低输出：

- 至少 `2` 次完整 mock
- 按 [scorecard.md](/Users/wizout/op/interview/practice/mock-interviews/scorecard.md) 打分并列弱项清单

## 只剩 7 天怎么压缩

1. 先过 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
2. 再过 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
3. 跑 [后端与系统设计口述速答包](/Users/wizout/op/interview/practice/drills/backend-and-system-design-oral-pack.md)
4. 做 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)
5. 跑 [后端场景压测包](/Users/wizout/op/interview/practice/drills/backend-scenario-pressure-pack.md)
6. 最后跑 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 社招最容易失分的地方

- 项目讲不出指标和取舍
- 故障题讲成流水账
- 系统设计只有组件图，没有容量和恢复策略
- 一追问就开始漂移，不会把答案拉回主线
