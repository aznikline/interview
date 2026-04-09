# Phase 4: System Design And Distributed Trade-offs

这个阶段是面试拉开差距的关键。目标不是画出最复杂的图，而是建立稳定的拆题和取舍框架。

## 阶段目标

- 能在不完整信息下澄清需求
- 能做粗粒度容量估算
- 能讲出架构选择的 trade-off
- 能补充故障处理和退化方案

## 建议时长

- 标准版：`10-14 天`
- 压缩版：`5-7 天`

## 推荐学习顺序

1. [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
2. [系统设计方法论](/Users/wizout/op/interview/docs/topics/system-design/01-system-design-methodology.md)
3. [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
4. [缓存一致性与流量治理](/Users/wizout/op/interview/docs/topics/system-design/02-cache-consistency-and-traffic.md)
5. [秒杀与高并发](/Users/wizout/op/interview/docs/topics/system-design/03-seckill-and-high-concurrency.md)
6. [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
7. [系统设计高频题](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
8. [系统设计案例题](/Users/wizout/op/interview/questions/system-design/design-cases.md)
9. [短链接案例](/Users/wizout/op/interview/projects/backend-case-studies/url-shortener.md)
10. [Feed 系统案例](/Users/wizout/op/interview/projects/design-case-studies/feed-system.md)
11. [秒杀系统案例](/Users/wizout/op/interview/projects/design-case-studies/seckill-system.md)

## 这阶段必须拿下的代表题

- 短链接系统
- 秒杀系统
- Feed 流
- 消息队列
- 分布式 ID
- 搜索建议系统

## 每周输出要求

### 输出 1：系统设计框架口述

先单独练框架，而不是上来就做题：

- 需求澄清
- 容量估算
- 高层架构
- 核心链路
- 瓶颈和 trade-off
- 故障与退化

### 输出 2：完整题目

至少完成 `2` 道完整系统设计题口述，每题控制在 `5-8 分钟`。

### 输出 3：项目迁移

把系统设计里的模式回挂到你的项目：

- 你项目里有没有缓存
- 有没有异步化
- 有没有热点或高并发问题
- 有没有一致性取舍

## 退出条件

- 不再一上来就堆组件
- 能完整讲 `2` 道题，并能接住追问
- 每道题都能讲出至少 `2` 个 trade-off

## 这个阶段最容易失败的方式

- 不做需求澄清
- 不做估算
- 只会说“加 Redis / 上 MQ / 分库分表”
- 只会讲 happy path，不会讲故障处理
