# 角色标签：基础架构 / 平台

## 适合谁

- 目标岗位是基础架构、中间件、平台服务、稳定性治理
- 日常工作偏流量治理、服务框架、缓存、MQ、链路可用性
- 面试里比通用后端更容易被追问到可靠性、故障恢复、性能排障

## 核心能力画像

- 一致性与幂等
- 限流、降级、熔断与恢复
- MQ、缓存、存储和高并发链路
- Linux 观测、网络 I/O、性能排查
- 能讲清事故、治理动作和复盘

## 推荐入口

- [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
- [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
- [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
- [可靠性与高并发深水区 Drill](/Users/wizout/op/interview/practice/drills/reliability-deep-dive.md)
- [可靠性与基础架构深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/reliability-and-infra.md)

## 正确起手顺序

1. 先过 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
2. 再过 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
3. 再补 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
4. 跑 [可靠性与高并发深水区 Drill](/Users/wizout/op/interview/practice/drills/reliability-deep-dive.md)
5. 做 [可靠性与基础架构深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/reliability-and-infra.md) 和 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 必须先保住的题

- 为什么很多业务不用强一致事务？
- 补偿、幂等、重试、对账分别负责什么？
- 为什么系统恢复阶段也可能再次被打崩？
- 为什么用了 epoll，服务还是会慢？
- 限流、熔断、降级分别该放在哪几层？
- 出现消息积压、热 key、慢请求时先看什么？

## 常见失分点

- 事故讲成时间线流水账，没有机制和判断
- 只会讲治理手段，不会讲为什么先做这一层
- 不会把指标、容量、恢复动作串起来
