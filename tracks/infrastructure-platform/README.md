# 基础架构 / 平台路线

适合：

- 目标岗位是基础架构、中间件、平台服务、流量治理、稳定性工程
- 面试重点更偏可用性、恢复策略、性能观测和大流量治理

## 核心准备顺序

1. 后端主链路
2. 操作系统与 Linux 排障
3. 系统设计里的恢复、限流、异步链路
4. 可靠性与高并发深水区训练
5. Mock 与追问承压

## 4 周起手计划

### Week 1：后端主链路

- [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- [后端场景地图](/Users/wizout/op/interview/docs/topics/backend/08-backend-scenario-map.md)

### Week 2：OS 与可观测性

- [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- [Linux 可观测性与性能排障](/Users/wizout/op/interview/docs/topics/operating-system/04-linux-observability-and-tuning.md)

### Week 3：恢复与故障处理

- [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
- [系统设计场景地图](/Users/wizout/op/interview/docs/topics/system-design/07-system-design-scenario-map.md)
- [可靠性与高并发深水区 Drill](/Users/wizout/op/interview/practice/drills/reliability-deep-dive.md)

### Week 4：承压训练

- [可靠性与基础架构深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/reliability-and-infra.md)
- [后端场景压测包](/Users/wizout/op/interview/practice/drills/backend-scenario-pressure-pack.md)
- [系统设计压测包](/Users/wizout/op/interview/practice/drills/system-design-pressure-pack.md)
- [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 最小交付标准

- 能讲一致性、补偿、恢复和限流是一套体系
- 能把 `epoll / 慢请求 / 上下文切换 / 观测指标` 连到真实故障
- 能讲一个事故或性能治理故事
