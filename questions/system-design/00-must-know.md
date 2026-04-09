# 系统设计核心题清单

## 题目

系统设计面试最该优先准备哪些题，顺序应该怎么排？

## 一句话回答

优先准备最能代表 `容量估算、缓存、一致性、异步解耦和高并发 trade-off` 的题：短链接、秒杀、Feed、消息队列、分布式 ID、搜索建议。顺序上先练答题框架，再练代表题，再练故障和 trade-off 追问。

## 展开回答

### 第一层：必须会讲的代表题

- 设计短链接系统
- 设计秒杀系统
- 设计 Feed 流
- 设计消息队列
- 设计全局唯一 ID 系统
- 设计搜索建议系统

### 第二层：每道题必须覆盖的结构

不管题目是什么，最低都要覆盖：

- 需求澄清
- 容量估算
- 数据模型
- 核心链路
- 高可用 / 扩展性
- trade-off
- 故障处理

### 第三层：建议练题顺序

1. 先看 [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
2. 再看 [系统设计方法论](/Users/wizout/op/interview/docs/topics/system-design/01-system-design-methodology.md)
3. 再看 [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
4. 然后刷 [系统设计高频题](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
5. 再刷 [系统设计案例题](/Users/wizout/op/interview/questions/system-design/design-cases.md)
6. 最后回到项目案例，补真实链路表达

### 第四层：最小交付标准

每道系统设计题至少要做到：

- `2 分钟` 内讲清整体框架
- `5-8 分钟` 内讲完整链路
- 至少补 `2` 个瓶颈点
- 至少补 `2` 个 trade-off

## 面试官追问

- 为什么容量估算不能省略？
- 为什么这题要上 MQ？
- 为什么这个场景选最终一致而不是强一致？
- 如果流量翻十倍，你先动哪一层？
- 如果缓存挂了，系统怎么退化？

## 易错点

- 一上来画组件图
- 不做估算
- 只讲“加 Redis / MQ”
- 只会讲 happy path，不讲故障和限流

## 关联知识点

- [系统设计专题首页](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
- [系统设计高频题](/Users/wizout/op/interview/questions/system-design/high-frequency.md)
- [系统设计进阶题](/Users/wizout/op/interview/questions/system-design/design-cases.md)
- [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
