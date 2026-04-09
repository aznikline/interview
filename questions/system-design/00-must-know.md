# 系统设计核心题清单

## 题目

系统设计面试最该优先准备哪些题？

## 一句话回答

优先准备最能代表容量估算、缓存、一致性、异步解耦和高并发取舍的题：短链接、秒杀、Feed、消息队列、分布式 ID、搜索建议。

## 展开回答

### 第一优先级：必须会讲

- 设计短链接系统
- 设计秒杀系统
- 设计 Feed 流
- 设计消息队列
- 设计全局唯一 ID 系统
- 设计搜索建议系统

### 每道题必须覆盖

- 需求澄清
- 容量估算
- 数据模型
- 核心链路
- 高可用 / 扩展性
- trade-off

## 面试官追问

- 为什么容量估算不能省略？
- 为什么这题要上 MQ？
- 为什么这个场景选最终一致而不是强一致？

## 易错点

- 一上来画组件图
- 不做估算
- 只讲“加 Redis / MQ”

## 关联知识点

- [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
- [系统设计高频题](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
- [系统设计进阶题](/Users/wizout/op/interview/questions/system-design/design-cases.md)

