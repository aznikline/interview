# 后端专题首页

## 1 分钟速答

后端面试的核心不是“背了多少组件”，而是你能不能把 `数据库`、`缓存`、`消息队列`、`分布式一致性`、`高并发链路` 和 `项目表达` 串成一条完整故事线。

## 核心机制

### 推荐学习顺序

1. 后端整体框架
2. MySQL 事务、锁、MVCC
3. Redis 与缓存一致性
4. MQ 可靠性与幂等
5. 系统设计答题法
6. 项目表达与 mock

### 必读文档

- [01-backend-fundamentals.md](/Users/wizout/op/interview/docs/topics/backend/01-backend-fundamentals.md)
- [02-mysql-transactions-and-locks.md](/Users/wizout/op/interview/docs/topics/backend/02-mysql-transactions-and-locks.md)
- [03-redis-and-cache-consistency.md](/Users/wizout/op/interview/docs/topics/backend/03-redis-and-cache-consistency.md)
- [04-mq-reliability-and-idempotency.md](/Users/wizout/op/interview/docs/topics/backend/04-mq-reliability-and-idempotency.md)
- [05-network-and-protocols.md](/Users/wizout/op/interview/docs/topics/backend/05-network-and-protocols.md)
- [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)

### 学完这一组内容后应该具备什么能力

- 能解释 MySQL、Redis、MQ 在链路里各解决什么问题
- 能讲清缓存一致性、幂等、补偿和限流这些真实工程问题
- 能把一个系统设计题连到你做过的项目

## 高频问法

- MySQL 为什么用 B+ 树？
- MVCC 解决了什么，边界在哪？
- 为什么更新数据库后通常删缓存？
- MQ 如何保证消息不丢和可重试？
- 分布式锁为什么经常不是最优解？

## 深挖与误区

- 不要把后端准备成“中间件名词背诵”
- 不要只会讲 happy path，不会讲失败场景
- 不要说项目很复杂，却给不出指标、容量和权衡

## 下一步

- 刷 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- 做 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)
