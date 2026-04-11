# 角色标签：通用后端

## 适合谁

- 目标岗位是通用后端、业务后端、平台后端
- 技术栈以 MySQL、Redis、MQ、Java / Go / C++ 服务为主
- 面试重点会落在链路治理、稳定性、系统设计和项目表达

## 核心能力画像

- 数据库与缓存
- 并发与网络
- 分布式链路治理
- 故障处理与稳定性
- 项目表达与系统设计

## 推荐入口

- [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
- [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- [后端与系统设计口述速答包](/Users/wizout/op/interview/practice/drills/backend-and-system-design-oral-pack.md)
- [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)

## 正确起手顺序

1. 先过 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md) 的主链路
2. 再补 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md) 里和服务性能最相关的部分
3. 再刷 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
4. 然后跑 [后端与系统设计口述速答包](/Users/wizout/op/interview/practice/drills/backend-and-system-design-oral-pack.md)
5. 最后做 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md) 和 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 必须先保住的题

- MySQL 为什么用 B+ 树？
- MVCC 和锁的边界是什么？
- 为什么通常删缓存而不是更新缓存？
- MQ 如何保证消息不丢、重复消费怎么处理？
- 为什么很多一致性问题不该先想到分布式锁？
- 设计一个高并发下单或秒杀链路

## 常见失分点

- 讲不出一个完整链路，只会碎片化背组件
- 讲不清 `代价 / 边界 / 监控指标`
- 系统设计和项目表达脱节
- 被追问到失败场景、补偿、故障恢复时开始空转

## 常见短板

- 只会背概念，不会讲链路
- 只会说组件，不会说 trade-off
- 不能把项目映射到高频系统设计题
