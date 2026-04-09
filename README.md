# Interview Engineering Repo

这是一个面向 `通用后端八股 + 算法 + 系统设计 + 操作系统 + AI 编译器` 的系统化面试工程。

它不是资料堆，也不是单纯题库，而是把这几类东西合成一个能持续复习和训练的仓库：

- `知识库`：按主题系统化梳理原理、答法、追问和误区
- `题库`：按高频问题组织标准回答和深挖路径
- `训练营`：按 30 天 / 60 天 / 角色方向组织复习计划
- `模拟面试`：把“知道”变成“能说”
- `项目案例`：把八股和系统设计映射到真实面试表达

## 这个仓库适合谁

- 准备 `通用后端` 面试的人
- 准备 `社招后端 / 基础架构` 面试的人
- 想系统补 `操作系统 + 分布式 + 系统设计` 的人
- 准备 `AI Infra / AI 编译器 / 推理优化` 方向的人

如果你是第一次打开这个仓库，先不要从文件树开始翻，先看下面的“第一次怎么用”。

## 第一次怎么用

### 方式 1：我只有 10 分钟，想先知道从哪里开始

按这个顺序看：

1. [总路线图](/Users/wizout/op/interview/docs/roadmap/00-overview.md)
2. [仓库地图](/Users/wizout/op/interview/docs/guides/repo-map.md)
3. 对应角色入口：
   [通用后端](/Users/wizout/op/interview/docs/interviews/role-tags/backend.md)
   [AI Infra / AI 编译器](/Users/wizout/op/interview/docs/interviews/role-tags/ai-infra.md)
4. [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)

### 方式 2：我准备后端面试，今天就想开始学

按这个顺序走：

1. [后端基础总览](/Users/wizout/op/interview/docs/topics/backend/01-backend-fundamentals.md)
2. [MySQL 事务与锁](/Users/wizout/op/interview/docs/topics/backend/02-mysql-transactions-and-locks.md)
3. [Redis 与缓存一致性](/Users/wizout/op/interview/docs/topics/backend/03-redis-and-cache-consistency.md)
4. [后端高频题](/Users/wizout/op/interview/questions/backend/high-frequency.md)
5. [后端进阶题](/Users/wizout/op/interview/questions/backend/distributed-and-db.md)
6. [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)

### 方式 3：我准备 AI Infra / AI 编译器方向

按这个顺序走：

1. [AI 编译器核心知识](/Users/wizout/op/interview/docs/topics/ai-compiler/01-ai-compiler-core.md)
2. [IR、Lowering 与 Dialect](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)
3. [Kernel 融合与 Runtime 协同](/Users/wizout/op/interview/docs/topics/ai-compiler/03-kernel-fusion-and-runtime.md)
4. [AI 编译器高频题](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
5. [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
6. [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)

## 推荐使用方式

### 如果你是 30 天冲刺

直接从 [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md) 开始。

建议节奏：

- 每天 1 篇 topic
- 每天 1 份 question set
- 每天至少口述 3 道题
- 每周 1 次 mock
- 每周 1 次复盘

### 如果你是长期积累

按这个顺序：

1. `roadmap` 确定优先级
2. `topics` 建立体系
3. `questions` 转成可回答能力
4. `practice` 检验表达
5. `projects` 训练项目化叙述

### 如果你已经有项目经验，但面试说不出来

重点看：

- [面试回答方法论](/Users/wizout/op/interview/docs/guides/answer-methodology.md)
- [面试策略](/Users/wizout/op/interview/docs/guides/interview-strategy.md)
- [Mock 评分卡](/Users/wizout/op/interview/practice/mock-interviews/scorecard.md)
- [系统设计案例](/Users/wizout/op/interview/projects/design-case-studies/seckill-system.md)
- [AI Runtime 调度案例](/Users/wizout/op/interview/projects/ai-compiler-case-studies/runtime-scheduling.md)

## 仓库结构不是干什么的，而是怎么用的

```text
interview/
├── docs/       # 先读这里，建立知识体系和路线图
├── questions/  # 然后刷这里，把知识点转成标准回答
├── tracks/     # 不想自己排计划时，直接照这个走
├── practice/   # 用来 mock、drill、打分、复盘
├── projects/   # 把知识点映射成项目表达和系统设计案例
├── scripts/    # 维护仓库用：生成索引、面板、lint
├── tests/      # 校验脚本没坏
└── data/       # 来源、标签、统计结果
```

## 你应该先看哪些文件

最小入口：

- [docs/roadmap/00-overview.md](/Users/wizout/op/interview/docs/roadmap/00-overview.md)
- [docs/guides/repo-map.md](/Users/wizout/op/interview/docs/guides/repo-map.md)
- [docs/guides/review-checklists.md](/Users/wizout/op/interview/docs/guides/review-checklists.md)

按岗位入口：

- [docs/interviews/role-tags/backend.md](/Users/wizout/op/interview/docs/interviews/role-tags/backend.md)
- [docs/interviews/role-tags/ai-infra.md](/Users/wizout/op/interview/docs/interviews/role-tags/ai-infra.md)
- [docs/interviews/company-tags/internet-platforms.md](/Users/wizout/op/interview/docs/interviews/company-tags/internet-platforms.md)

按训练入口：

- [tracks/sprint-30d/day-by-day.md](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)
- [practice/mock-interviews/backend-general.md](/Users/wizout/op/interview/practice/mock-interviews/backend-general.md)
- [practice/mock-interviews/ai-infra.md](/Users/wizout/op/interview/practice/mock-interviews/ai-infra.md)

## 当前仓库已经覆盖到什么程度

- `topics`：总览 + 专题深挖
- `questions`：基础高频 + 进阶追问
- `tracks`：30 天、60 天、校招、社招、AI Infra
- `practice`：4+ 份 mock、评分卡、drill、复盘模板
- `projects`：后端系统设计案例 + AI 编译器 / runtime 案例
- `data/sources`：GitHub 面经索引 + AI 编译器官方仓库 / 官方文档

## 内容标准

- 每个主题文档都包含：`1 分钟速答`、`核心机制`、`高频问法`、`深挖与误区`
- 每道题都包含：`题目`、`一句话回答`、`展开回答`、`面试官追问`
- 每个系统设计案例都包含：`需求澄清`、`容量估算`、`核心组件`、`瓶颈与 trade-off`
- AI 编译器部分同时覆盖：`图编译`、`算子优化`、`运行时协同`、`硬件适配`

## 数据来源策略

仓库正文以 `重写和抽象` 为主，不直接复制外部内容。

- GitHub 面经 / 题库 / CS 知识仓库用于建立题源和索引
- 官方仓库与官方文档用于 AI 编译器专题的一手信息
- 微信文章里的题目只作为问题池补充，不直接照搬为正文

来源总表见 [data/sources/source-index.md](/Users/wizout/op/interview/data/sources/source-index.md)。

## 如果你想维护这个仓库

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python scripts/build_index.py
python scripts/sync_sources.py
python scripts/generate_progress.py
python scripts/lint_docs.py
pytest
```

CI 已配置在 [ci.yml](/Users/wizout/op/interview/.github/workflows/ci.yml)。
