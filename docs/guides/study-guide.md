# 学习指南

这个仓库现在按“在线教程”的方式组织：先给你入口和时间线，再给路线图，再给主题教程、题单和训练闭环。

如果你第一次使用，建议先看：

1. [Start Here](../START-HERE.md)
2. [总路线图](../roadmap/00-overview.md)
3. 你的方向首页
4. 对应方向的核心题清单

## 如果你只有 3 天

### Day 1

- 后端：MySQL、Redis、MQ 三件套
- OS：进程线程、内存、I/O
- 输出：每个主题至少说出 `3 个高频题`

建议入口：

- [后端专题首页](../topics/backend/00-index.md)
- [操作系统专题首页](../topics/operating-system/00-index.md)
- [后端核心题清单](../../questions/backend/00-must-know.md)

### Day 2

- 系统设计：容量估算、缓存、一致性、高并发
- 算法：滑动窗口、双指针、二叉树、DP
- 输出：能完整口述 `1 道系统设计题 + 2 道算法题`

建议入口：

- [系统设计答题法](how-to-approach-system-design.md)
- [算法框架与训练法](../topics/algorithm/03-frameworks-and-drills.md)
- [系统设计核心题清单](../../questions/system-design/00-must-know.md)

### Day 3

- AI 编译器：整体链路、IR、lowering、fusion、runtime
- 项目表达：挑 1 个后端项目和 1 个 AI Infra 项目做故事化表达
- 输出：做 1 次 mock

建议入口：

- [AI 编译器入门章节](../topics/ai-compiler/04-getting-started-and-chapters.md)
- [AI 编译器答题法](how-to-approach-ai-compiler-interview.md)
- [AI 编译器项目表达稿](../../projects/ai-compiler-case-studies/project-storytelling.md)

## 如果你有 1 周

直接跑 [7 天急救计划](../../practice/drills/7-day-rescue-plan.md)。

这一周的目标不是“覆盖一切”，而是完成最小闭环：

- 后端能讲主链路
- OS 能讲原理和权衡
- 系统设计能讲结构和取舍
- 算法能口述思路和复杂度
- AI 编译器能讲层次边界和指标

## 如果你有 1 个月

直接跑 [30 天逐日执行表](../../tracks/sprint-30d/day-by-day.md)。

这 30 天的输出标准应该是：

- 每周完成 `1 次 mock`
- 每周完成 `1 次复盘`
- 每个领域至少形成 `10 个可直接口述的问题答案`
- 至少能讲出 `2 个项目故事`

## 如果你有 2 个月

从 [60 天路径](../../tracks/sprint-60d/README.md) 开始。

这条路径更适合：

- 基础一般，但希望从零补齐体系的人
- 想把知识点从“会背”提升到“会讲、会追问、会连接项目”的人

## 三条学习顺序原则

### 1. 先做主线，再补枝叶

后端先抓 `数据库 -> 缓存 -> MQ -> 一致性 -> 高并发`。
AI 编译器先抓 `IR -> lowering -> fusion -> runtime -> 指标`。

### 2. 先会讲，再做深挖

先把 `1 分钟回答` 练顺，再补 `5 分钟深挖`。一开始就钻细节，很容易把自己准备成碎片化知识。

### 3. 先形成输出，再继续扩题库

每看完一篇文档，要么去刷题，要么去 mock，要么去复盘。只看不输出，基本等于没学。

## 每个阶段应该产出什么

### 看完 topics

- 你应该能讲清“这部分解决什么问题”
- 你应该能列出 `3-5` 个高频问法

### 刷完 questions

- 你应该能按模板回答
- 你应该能处理 1-2 个追问

### 做完 practice

- 你应该能发现自己最容易断掉的地方
- 你应该能知道下周要补什么

### 看完 projects

- 你应该能把知识点挂到实际项目上
- 你应该能把设计取舍和指标收益讲出来
