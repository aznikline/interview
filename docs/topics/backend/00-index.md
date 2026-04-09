# 后端专题首页

## 1 分钟速答

后端面试最重要的不是单个知识点，而是你能否把 `数据库`、`缓存`、`消息队列`、`分布式一致性`、`高并发链路` 讲成一条完整故事线。准备顺序应该是先打基础，再做并发与分布式，再做项目表达。

## 核心机制

### 推荐学习顺序

1. 后端基础总览
2. MySQL 事务、锁、MVCC
3. Redis 与缓存一致性
4. MQ 可靠性与幂等
5. 分布式链路与项目表达

### 必读文档

- [01-backend-fundamentals.md](/Users/wizout/op/interview/docs/topics/backend/01-backend-fundamentals.md)
- [02-mysql-transactions-and-locks.md](/Users/wizout/op/interview/docs/topics/backend/02-mysql-transactions-and-locks.md)
- [03-redis-and-cache-consistency.md](/Users/wizout/op/interview/docs/topics/backend/03-redis-and-cache-consistency.md)
- [04-mq-reliability-and-idempotency.md](/Users/wizout/op/interview/docs/topics/backend/04-mq-reliability-and-idempotency.md)

## 高频问法

- MySQL 为什么用 B+ 树？
- MVCC 解决了什么？
- 缓存一致性怎么做？
- MQ 如何保证消息不丢？
- 分布式锁为什么常常不是最优解？

## 深挖与误区

- 不要把后端准备成“组件背诵”
- 不要只会说“用了 Redis / MQ”
- 必须能从项目里举出高并发、稳定性或一致性的真实例子

## 下一步

- 刷 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- 跑 [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)

