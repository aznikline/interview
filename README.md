# 面试总手册

一个面向 `后端 / 算法 / 系统设计 / 操作系统 / LLM / AI Infra / AI 编译器` 的长期面试工程。

这个仓库现在不是“资料堆”，而是两层结构：

- `手册整合层`
  负责把知识点、题单、路线、drill、mock 组织成可学习、可输出、可复习的手册。
- `原始参考层`
  负责把外部原始仓库一比一挂接在 `references/` 下，保留完整目录结构，避免只剩二手摘要。

## 先看什么

### 1. 第一次进入仓库

- [Start Here](docs/START-HERE.md)
- [总路线图](docs/roadmap/00-overview.md)
- [参考源总目录](docs/reference/00-source-layer.md)

### 2. 先按目标岗位选入口

- [通用后端](docs/interviews/role-tags/backend.md)
- [基础架构 / 平台](docs/interviews/role-tags/infrastructure-platform.md)
- [AI Infra](docs/interviews/role-tags/ai-infra.md)
- [AI 编译器](docs/interviews/role-tags/ai-compiler.md)
- [LLM 算法 / 应用工程](docs/interviews/role-tags/llm-engineer.md)

### 3. 先按可执行路线选入口

- [校招路线](tracks/campus/README.md)
- [社招路线](tracks/social-hire/README.md)
- [基础架构 / 平台路线](tracks/infrastructure-platform/README.md)
- [AI Infra 路线](tracks/ai-infra/README.md)
- [LLM 路线](tracks/llm-engineer/README.md)
- [Interview University 学习计划](tracks/interview-university/README.md)

### 4. 如果时间不够

- [7 天急救计划](practice/drills/7-day-rescue-plan.md)
- [30 天逐日执行表](tracks/sprint-30d/day-by-day.md)
- [Last 24 Hours](tracks/interview-university/last-24-hours.md)

## 两层结构

### 手册整合层

这一层是你真正用来学习和准备面试的内容：

- `docs/topics`
- `questions`
- `tracks`
- `practice`
- `projects`

它解决的是：

- 该先学什么
- 该先保哪些题
- 每一块怎么练成面试输出

### 原始参考层

这一层是你要求的“原始仓库完整接入层”，现在在 `references/`：

- [参考源总目录](docs/reference/00-source-layer.md)
- [LLM 参考源索引](docs/reference/01-llm-source-index.md)
- [AI Infra 参考源索引](docs/reference/02-ai-infra-source-index.md)
- [LLM 章节树](docs/reference/03-llm-reference-tree.md)
- [AI Infra 章节树](docs/reference/04-ai-infra-reference-tree.md)
- [整合层与原始层映射](docs/reference/05-handbook-to-reference-map.md)

它解决的是：

- 想看原始目录时，直接进源仓库
- 想对照手册和原始章节时，有映射表可查
- 想从源码、项目、文档细节回补时，有明确入口

## 主目录

### 00. 使用说明

- [Start Here](docs/START-HERE.md)
- [总路线图](docs/roadmap/00-overview.md)
- [学习指南](docs/guides/study-guide.md)
- [答题方法论](docs/guides/answer-methodology.md)

### 01. 后端

- [专题首页](docs/topics/backend/00-index.md)
- [核心题清单](questions/backend/00-must-know.md)
- [代表题清单](questions/backend/representative-scenarios.md)
- [场景地图](docs/topics/backend/08-backend-scenario-map.md)
- [14 天计划](tracks/backend-scenario-14d/README.md)
- [压测包](practice/drills/backend-scenario-pressure-pack.md)

### 02. 算法

- [专题首页](docs/topics/algorithm/00-index.md)
- [核心题清单](questions/algorithm/00-must-know.md)
- [代表题清单](questions/algorithm/labuladong-representative-problems.md)
- [模式地图](docs/topics/algorithm/05-labuladong-pattern-map.md)
- [Quick Master](docs/topics/algorithm/06-quick-master-index.md)
- [14 天计划](tracks/algorithm-pattern-14d/README.md)
- [压测包](practice/drills/algorithm-pattern-pressure-pack.md)

### 03. 操作系统

- [专题首页](docs/topics/operating-system/00-index.md)
- [核心题清单](questions/operating-system/00-must-know.md)
- [代表题清单](questions/operating-system/representative-scenarios.md)
- [场景地图](docs/topics/operating-system/06-os-scenario-map.md)
- [14 天计划](tracks/os-14d/README.md)
- [压测包](practice/drills/os-pressure-pack.md)

### 04. 系统设计

- [专题首页](docs/topics/system-design/00-index.md)
- [核心题清单](questions/system-design/00-must-know.md)
- [代表题清单](questions/system-design/representative-scenarios.md)
- [场景地图](docs/topics/system-design/07-system-design-scenario-map.md)
- [14 天计划](tracks/system-design-14d/README.md)
- [压测包](practice/drills/system-design-pressure-pack.md)

### 05. AI Infra / AI 编译器 / LLM

- [AI Infra 专题首页](docs/topics/ai-infra/00-index.md)
- [AI 编译器专题首页](docs/topics/ai-compiler/00-index.md)
- [LLM 面试专题首页](docs/topics/llm/00-index.md)
- [AI Infra 路线](tracks/ai-infra/README.md)
- [LLM 路线](tracks/llm-engineer/README.md)

### 06. Drill / Mock / 冲刺

- [每日 Drill](practice/drills/daily-drill.md)
- [追问压测包](practice/drills/follow-up-pressure-pack.md)
- [Final Review Checklist](tracks/interview-university/final-review.md)
- [Last 24 Hours](tracks/interview-university/last-24-hours.md)
- [评分卡](practice/mock-interviews/scorecard.md)

### 99. 参考资料

- [来源索引](data/sources/source-index.md)
- [参考源总目录](docs/reference/00-source-layer.md)
- [仓库地图](docs/guides/repo-map.md)

## 这个仓库现在解决什么问题

- 从“刷过很多，但讲不顺”到“能稳定输出”
- 从“只有二手笔记”到“手册层 + 原始层”双层闭环
- 从“AI Infra / LLM / 编译器混成一坨”到三条主线分开又能互相映射

## 使用边界

- 手册正文以原创整理和结构化重写为主
- `references/` 保留原始仓库结构，作为原始层
- 原始仓库是参考源，不直接等于你的面试答案
