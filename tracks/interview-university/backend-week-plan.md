# Backend Week Plan

适用场景：

- 你要在 `5-7` 天内把后端主链路快速讲顺
- 你准备先保后端一面，再补其他模块

## Day 1：MySQL

- 阅读 [02-mysql-transactions-and-locks.md](../../docs/topics/backend/02-mysql-transactions-and-locks.md)
- 回答：
  - MySQL 为什么用 B+ 树
  - MVCC 解决了什么
  - redo / undo / binlog 区别
- 输出：录一段 `3-5` 分钟口述

## Day 2：Redis 与缓存

- 阅读 [03-redis-and-cache-consistency.md](../../docs/topics/backend/03-redis-and-cache-consistency.md)
- 回答：
  - Redis 为什么快
  - 缓存穿透 / 击穿 / 雪崩
  - 更新数据库后为什么通常删缓存
- 输出：写一版缓存一致性答题模板

## Day 3：MQ 与幂等

- 阅读 [04-mq-reliability-and-idempotency.md](../../docs/topics/backend/04-mq-reliability-and-idempotency.md)
- 回答：
  - 如何保证消息不丢
  - 至少一次为什么会重复消费
  - 幂等如何落地
- 输出：口述 `消息不丢 -> 重复消费 -> 幂等` 三连

## Day 4：链路串讲

- 回看 [后端核心题清单](../../questions/backend/00-must-know.md)
- 练习把 `MySQL -> Redis -> MQ -> 一致性 -> 高并发` 串成一条故事线
- 输出：完整口述一次

## Day 5：项目连接

- 选一个后端项目
- 回答：
  - 请求怎么进来
  - 数据怎么落
  - 为什么加缓存
  - 为什么异步化
  - 遇到过什么热点或故障
- 输出：项目表达稿初版

## Day 6：系统设计连接

- 阅读 [系统设计答题法](../../docs/guides/how-to-approach-system-design.md)
- 把后端主链路知识点挂到秒杀或下单题
- 输出：`5-8` 分钟系统设计口述一次

## Day 7：Mock 与复盘

- 做 [backend-general.md](../../practice/mock-interviews/backend-general.md) 或 [senior-backend.md](../../practice/mock-interviews/senior-backend.md)
- 用 [scorecard.md](../../practice/mock-interviews/scorecard.md) 打分
- 输出：弱项清单
