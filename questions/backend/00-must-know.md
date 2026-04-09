# 后端核心题清单

## 题目

后端面试最应该优先刷哪些题，顺序应该怎么排？

## 一句话回答

先刷能串成完整工程链路的题：`MySQL -> Redis -> MQ -> 一致性 -> 高并发 -> 项目表达`。顺序上先抓主链路，再补追问，再补系统设计连接点。

## 展开回答

### 第一层：必须先拿下的 8 题

这 8 题是主链路，优先级最高：

- MySQL 为什么用 B+ 树？
- MVCC 解决了什么？为什么读写能并发？
- 索引失效有哪些典型场景？
- Redis 为什么快？边界在哪里？
- 缓存穿透、击穿、雪崩分别怎么治理？
- 更新数据库后为什么通常删缓存？
- MQ 如何保证消息不丢？
- 讲一个你做过的高并发或稳定性项目

如果这 8 题讲不顺，后面的追问很难接住。

### 第二层：必须能接住的追问

- redo log、undo log、binlog 的区别
- 可重复读为什么还能防幻读
- 行锁、间隙锁、next-key lock 的区别
- 热 key、大 key、慢查询、消息积压怎么排查
- 至少一次为什么一定会带来重复消费
- 幂等在业务里到底怎么落地

### 第三层：要能连到系统设计的题

- 分布式锁为什么经常不是最优解
- 如何设计秒杀/下单链路
- 如何做限流、熔断、降级
- 一致性为什么没有银弹
- 时钟回拨为什么会影响分布式 ID

### 建议刷题顺序

1. 先看 [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
2. 再看 MySQL、Redis、MQ 三篇专题
3. 再刷 [后端高频题](/Users/wizout/op/interview/questions/backend/high-frequency.md)
4. 再刷 [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
5. 最后做 1 次 mock，把这些题串成链路

### 每题最低输出标准

每道题至少要能说出：

- 一个 `1 分钟回答`
- 两个 `追问`
- 一个 `工程案例`
- 一个 `边界或反例`

## 面试官追问

- 如果只给你 30 分钟准备，你先保哪 5 题？
- 如果项目不强，怎么靠这些题稳住一面？
- 哪些题最适合连到系统设计？
- 哪些题最容易被问到故障处理？

## 易错点

- 只会背组件，不会讲链路
- 只会讲 happy path，不会讲故障与补偿
- 只会说“项目很复杂”，却说不出指标和取舍

## 关联知识点

- [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
- [后端高频题](/Users/wizout/op/interview/questions/backend/high-frequency.md)
- [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
- [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
