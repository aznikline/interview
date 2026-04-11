# System Design Week Plan

适用场景：

- 你有一周时间专门补系统设计
- 你已经有后端基础，但系统设计答题不成形

## Day 1：答题框架

- 阅读 [系统设计答题法](../../docs/guides/how-to-approach-system-design.md)
- 输出：只练框架，不做具体题
- 要求：`2` 分钟内讲清需求、估算、架构、链路、trade-off、故障

## Day 2：短链接

- 阅读 [url-shortener.md](../../projects/backend-case-studies/url-shortener.md)
- 输出：完整讲一遍短链接题
- 重点：编码、冲突、热点、读写分离

## Day 3：秒杀

- 阅读 [03-seckill-and-high-concurrency.md](../../docs/topics/system-design/03-seckill-and-high-concurrency.md)
- 阅读 [seckill-system.md](../../projects/design-case-studies/seckill-system.md)
- 输出：讲清削峰、限流、库存一致性

## Day 4：Feed

- 阅读 [feed-system.md](../../projects/design-case-studies/feed-system.md)
- 输出：讲清 pull / push / hybrid

## Day 5：高频题串讲

- 阅读 [系统设计核心题清单](../../questions/system-design/00-must-know.md)
- 刷 [系统设计高频题](../../questions/system-design/high-frequency.md)
- 输出：至少完成 `2` 道题口述

## Day 6：故障和 trade-off

- 专门补：
  - 缓存挂了怎么办
  - MQ 积压怎么办
  - 热点怎么办
  - 流量翻十倍先动哪一层
- 输出：为两道题各补 `2` 个故障场景

## Day 7：Mock 与复盘

- 做一次完整系统设计 mock
- 用 [scorecard.md](../../practice/mock-interviews/scorecard.md) 打分
- 输出：最不稳的 `3` 道题和最弱的 `3` 个环节
