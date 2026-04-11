# Phase 1: Backend Core

这个阶段解决一个核心问题：把后端主链路讲顺。

很多人面试输在“每个点都知道一点，但串不起来”。这个阶段就是要把数据库、缓存、消息队列、一致性和高并发问题压成一条稳定叙事线。

## 阶段目标

- 讲清 MySQL、Redis、MQ 在链路中各自解决什么问题
- 能回答一致性、幂等、限流、降级这些典型工程问题
- 能把知识点连到你自己的项目

## 建议时长

- 标准版：`10-14 天`
- 压缩版：`5-7 天`

## 推荐学习顺序

1. [后端专题首页](../../docs/topics/backend/00-index.md)
2. [后端基础总览](../../docs/topics/backend/01-backend-fundamentals.md)
3. [MySQL 事务、锁与 MVCC](../../docs/topics/backend/02-mysql-transactions-and-locks.md)
4. [Redis 与缓存一致性](../../docs/topics/backend/03-redis-and-cache-consistency.md)
5. [MQ 可靠性与幂等](../../docs/topics/backend/04-mq-reliability-and-idempotency.md)
6. [后端核心题清单](../../questions/backend/00-must-know.md)
7. [后端高频题](../../questions/backend/high-frequency.md)
8. [后端进阶题](../../questions/backend/distributed-and-db.md)

## 这阶段必须拿下的核心问题

- MySQL 为什么用 B+ 树？
- MVCC 解决了什么？
- redo log、undo log、binlog 分别干什么？
- 更新数据库后为什么通常删缓存？
- Redis 快在哪里，边界在哪里？
- MQ 如何保证消息不丢？
- 幂等如何落地？
- 分布式锁什么时候不该用？
- 如何设计高并发下单或秒杀链路？

## 每周输出要求

### 输出 1：主链路口述

至少完成一次 `MySQL -> Redis -> MQ -> 一致性 -> 高并发` 的完整口述，控制在 `5-8 分钟`。

### 输出 2：项目连接

挑你自己的一个项目，回答这几个问题：

- 数据是怎么落的
- 缓存为什么要这么设计
- 异步化在哪里
- 一致性如何兜底
- 指标提升体现在哪里

### 输出 3：mock

至少完成一次 [backend-general.md](../../practice/mock-interviews/backend-general.md) 或 [senior-backend.md](../../practice/mock-interviews/senior-backend.md)。

## 退出条件

- 能稳定讲 `8-10` 个后端高频问题
- 被追问到锁、日志、幂等、热 key、消息积压时不会直接断掉
- 至少有 `1` 个项目例子可以把这些知识点串起来

## 这个阶段最容易失败的方式

- 只背组件定义，不讲链路
- 只会讲 happy path，不讲失败场景
- 只讲“用了 Redis / MQ”，却说不出为什么
- 说项目复杂，但没有指标、容量和 trade-off
