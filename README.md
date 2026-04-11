# 面试手册：后端 / 算法 / 系统设计 / OS / LLM / AI Infra / AI 编译器

## 简介

这个仓库不是散装资料夹，也不是只会堆链接的面经目录。

它现在被重写成一份 `手册型` 面试工程，目标是把下面几条主线真正组织成可读、可练、可复习的知识体系：

- 通用后端
- 算法与数据结构
- 系统设计
- 操作系统与性能
- LLM 面试
- AI Infra / AI 编译器

参考过的成熟仓库组织方式包括：

- [coding-interview-university](https://github.com/jwasham/coding-interview-university)
- [system-design-primer](https://github.com/donnemartin/system-design-primer)
- [wdndev/llm_interview_note](https://github.com/wdndev/llm_interview_note)

但这个仓库最终解决的是你自己的问题：

- 已经做过业务，但知识体系是碎的
- 刷过题，但不会口述、不会追问、不会把题连到项目
- 想补 AI Infra / AI 编译器差异化方向，但不想失去后端主线

## 怎么开始

### 方式 1：按岗位进入

- [通用后端](docs/interviews/role-tags/backend.md)
- [基础架构 / 平台](docs/interviews/role-tags/infrastructure-platform.md)
- [AI Infra](docs/interviews/role-tags/ai-infra.md)
- [AI 编译器](docs/interviews/role-tags/ai-compiler.md)

### 方式 2：按路线进入

- [校招路线](tracks/campus/README.md)
- [社招路线](tracks/social-hire/README.md)
- [基础架构 / 平台路线](tracks/infrastructure-platform/README.md)
- [AI Infra 路线](tracks/ai-infra/README.md)
- [Interview University 学习计划](tracks/interview-university/README.md)

### 方式 3：按时间进入

- [7 天急救计划](practice/drills/7-day-rescue-plan.md)
- [30 天逐日执行表](tracks/sprint-30d/day-by-day.md)
- [Last 24 Hours](tracks/interview-university/last-24-hours.md)

## 双层结构

### 01. 手册整合层

也就是 `docs/topics`、`questions`、`tracks`、`practice`。这里负责：

- 把知识点讲清
- 把题目按逻辑收口
- 把路线和 drill 跑通

### 02. 原始参考层

也就是 `references/`。这里直接挂接外部原始仓库，保留它们完整目录结构：

- [参考源总目录](docs/reference/00-source-layer.md)
- [LLM 参考源索引](docs/reference/01-llm-source-index.md)
- [AI Infra 参考源索引](docs/reference/02-ai-infra-source-index.md)

## 目录

### 00. 使用说明

- [Start Here](docs/START-HERE.md)
- [总路线图](docs/roadmap/00-overview.md)
- [学习指南](docs/guides/study-guide.md)
- [答题方法论](docs/guides/answer-methodology.md)

### 01. 后端主线

- [后端专题首页](docs/topics/backend/00-index.md)
- [后端核心题清单](questions/backend/00-must-know.md)
- [后端高频题](questions/backend/high-frequency.md)
- [后端进阶题](questions/backend/distributed-and-db.md)
- [后端代表题清单](questions/backend/representative-scenarios.md)
- [后端场景地图](docs/topics/backend/08-backend-scenario-map.md)
- [后端场景 14 天计划](tracks/backend-scenario-14d/README.md)
- [后端场景压测包](practice/drills/backend-scenario-pressure-pack.md)

### 02. 算法与数据结构

- [算法专题首页](docs/topics/algorithm/00-index.md)
- [算法核心题清单](questions/algorithm/00-must-know.md)
- [算法高频题](questions/algorithm/high-frequency.md)
- [算法进阶题](questions/algorithm/patterns-and-dp.md)
- [算法代表题清单](questions/algorithm/labuladong-representative-problems.md)
- [算法模式地图](docs/topics/algorithm/05-labuladong-pattern-map.md)
- [Quick Master 冲刺索引](docs/topics/algorithm/06-quick-master-index.md)
- [算法模式 14 天计划](tracks/algorithm-pattern-14d/README.md)
- [算法模式压测包](practice/drills/algorithm-pattern-pressure-pack.md)

### 03. 操作系统与性能

- [操作系统专题首页](docs/topics/operating-system/00-index.md)
- [操作系统核心题清单](questions/operating-system/00-must-know.md)
- [OS 高频题](questions/operating-system/high-frequency.md)
- [OS 进阶题](questions/operating-system/concurrency-and-memory.md)
- [OS 代表题清单](questions/operating-system/representative-scenarios.md)
- [OS 场景地图](docs/topics/operating-system/06-os-scenario-map.md)
- [OS 14 天计划](tracks/os-14d/README.md)
- [OS 压测包](practice/drills/os-pressure-pack.md)

### 04. 系统设计

- [系统设计专题首页](docs/topics/system-design/00-index.md)
- [系统设计核心题清单](questions/system-design/00-must-know.md)
- [系统设计高频题](questions/system-design/high-frequency.md)
- [系统设计进阶题](questions/system-design/design-cases.md)
- [系统设计代表题清单](questions/system-design/representative-scenarios.md)
- [系统设计场景地图](docs/topics/system-design/07-system-design-scenario-map.md)
- [系统设计 14 天计划](tracks/system-design-14d/README.md)
- [系统设计压测包](practice/drills/system-design-pressure-pack.md)

### 05. AI Infra

- [AI Infra 专题首页](docs/topics/ai-infra/00-index.md)
- [AI Infra 核心题清单](questions/ai-infra/00-must-know.md)
- [AI Infra 高频题](questions/ai-infra/high-frequency.md)
- [AI Infra 代表题清单](questions/ai-infra/representative-scenarios.md)
- [AI Infra 21 天计划](tracks/ai-infra-21d/README.md)
- [AI Infra 压测包](practice/drills/ai-infra-pressure-pack.md)

### 05A. AI 编译器

- [AI 编译器专题首页](docs/topics/ai-compiler/00-index.md)
- [AI 编译器核心题清单](questions/ai-compiler/00-must-know.md)
- [AI 编译器高频题](questions/ai-compiler/high-frequency.md)
- [AI 编译器进阶题](questions/ai-compiler/deep-dive.md)
- [AI 编译器答题法](docs/guides/how-to-approach-ai-compiler-interview.md)
- [OS 与 AI 编译器口述速答包](practice/drills/os-and-ai-compiler-oral-pack.md)
- [AI 编译器深挖 Mock](practice/mock-interviews/ai-compiler-deep-dive.md)

### 05B. LLM 面试

- [LLM 面试专题首页](docs/topics/llm/00-index.md)
- [LLM 核心题清单](questions/llm/00-must-know.md)
- [LLM 高频题](questions/llm/high-frequency.md)
- [LLM 代表题清单](questions/llm/representative-scenarios.md)
- [LLM 21 天计划](tracks/llm-interview-21d/README.md)
- [LLM 压测包](practice/drills/llm-pressure-pack.md)

### 06. Drill / Mock / 压测

- [每日 Drill](practice/drills/daily-drill.md)
- [后端与系统设计口述速答包](practice/drills/backend-and-system-design-oral-pack.md)
- [算法口述速答包](practice/drills/algorithm-oral-pack.md)
- [OS 与 AI 编译器口述速答包](practice/drills/os-and-ai-compiler-oral-pack.md)
- [追问压测包](practice/drills/follow-up-pressure-pack.md)
- [资深后端 Mock](practice/mock-interviews/senior-backend.md)
- [AI Infra Mock](practice/mock-interviews/ai-infra.md)
- [评分卡](practice/mock-interviews/scorecard.md)

### 07. 角色与路线

- [通用后端](docs/interviews/role-tags/backend.md)
- [基础架构 / 平台](docs/interviews/role-tags/infrastructure-platform.md)
- [AI Infra](docs/interviews/role-tags/ai-infra.md)
- [AI 编译器](docs/interviews/role-tags/ai-compiler.md)
- [LLM 算法 / 应用工程](docs/interviews/role-tags/llm-engineer.md)
- [校招路线](tracks/campus/README.md)
- [社招路线](tracks/social-hire/README.md)
- [基础架构 / 平台路线](tracks/infrastructure-platform/README.md)
- [AI Infra 路线](tracks/ai-infra/README.md)

### 08. 冲刺与复习

- [Final Review Checklist](tracks/interview-university/final-review.md)
- [Closer To The Interview](tracks/interview-university/closer-to-interview.md)
- [Last 3 Days](tracks/interview-university/last-3-days.md)
- [Last 24 Hours](tracks/interview-university/last-24-hours.md)
- [Interview Day Checklist](tracks/interview-university/interview-day.md)

### 99. 参考资料

- [来源索引](data/sources/source-index.md)
- [仓库地图](docs/guides/repo-map.md)
- [在线教程结构参考](docs/guides/online-tutorial-patterns.md)
- [参考源总目录](docs/reference/00-source-layer.md)
- [LLM 参考源索引](docs/reference/01-llm-source-index.md)
- [AI Infra 参考源索引](docs/reference/02-ai-infra-source-index.md)

## 推荐使用方式

### 如果你是第一次来

1. 先看 [Start Here](docs/START-HERE.md)
2. 再选岗位入口或路线入口
3. 然后从对应领域的 `专题首页 -> 核心题清单 -> 代表题清单 -> 14 天计划 -> 压测包` 开始

### 如果你只剩 1 周

1. 跑 [7 天急救计划](practice/drills/7-day-rescue-plan.md)
2. 跑对应领域的 `口述速答包`
3. 跑 [追问压测包](practice/drills/follow-up-pressure-pack.md)
4. 用 [评分卡](practice/mock-interviews/scorecard.md) 打分

### 如果你只剩 1 天

直接看：

- [Last 24 Hours](tracks/interview-university/last-24-hours.md)
- [Final Review Checklist](tracks/interview-university/final-review.md)
- 你自己的一页纸弱项清单

## 仓库定位

这个仓库现在明确不是：

- 散装资料站
- 只收集链接的仓库
- 只会堆大纲的空架子

它更像一份长期可迭代的 `面试手册 + 训练工程`：

- 用专题文档讲知识
- 用题单和代表题做收口
- 用 14 天计划形成短冲刺路线
- 用口述包、压测包和 mock 把知识压成面试输出

## 维护说明

- 正文内容以原创整理和结构化重写为主
- 在线教程和外部仓库只参考组织方式和主题覆盖，不直接复制正文
- 本地个人资料或题单缓存，只做索引和训练映射，不做整站复刻
