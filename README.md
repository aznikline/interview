# Interview Engineering Repo

这是一个面向 `通用后端八股 + 算法 + 系统设计 + 操作系统 + AI 编译器` 的系统化面试仓库。

它不应该只是“文档目录”，而应该帮你解决三个实际问题：

- `从哪开始`：第一次进仓库不迷路
- `先学什么`：不同方向有明确顺序
- `怎么练`：知识点、题目、mock、项目表达能形成闭环

## 先别往下翻，第一次用直接看这里

最短路径：

1. [Start Here](/Users/wizout/op/interview/docs/START-HERE.md)
2. [总路线图](/Users/wizout/op/interview/docs/roadmap/00-overview.md)
3. 选你的方向：
   [通用后端](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
   [算法](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
   [系统设计](/Users/wizout/op/interview/docs/topics/system-design/00-index.md)
   [操作系统](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
   [AI 编译器](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
4. 再刷你方向的核心题清单：
   [后端](/Users/wizout/op/interview/questions/backend/00-must-know.md)
   [算法](/Users/wizout/op/interview/questions/algorithm/00-must-know.md)
   [系统设计](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
   [操作系统](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
   [AI 编译器](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)

## 这个仓库适合谁

- 准备 `通用后端` 面试的人
- 准备 `社招后端 / 基础架构` 的人
- 想系统补 `操作系统 + 分布式 + 系统设计` 的人
- 准备 `AI Infra / AI 编译器 / 推理优化` 方向的人
- 面试快到了但不知道先刷什么的人

## 如果你时间很少

### 只有 1 周

直接执行 [7 天急救计划](/Users/wizout/op/interview/practice/drills/7-day-rescue-plan.md)。

### 有 1 个月

直接执行 [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)。

### 只是想先建立框架

按这个顺序：

1. [Start Here](/Users/wizout/op/interview/docs/START-HERE.md)
2. [仓库地图](/Users/wizout/op/interview/docs/guides/repo-map.md)
3. [复习检查清单](/Users/wizout/op/interview/docs/guides/review-checklists.md)

## 仓库结构不是“放什么”，而是“怎么用”

```text
interview/
├── docs/       # 学习入口、路线图、专题首页、方法论
├── questions/  # 核心题清单 + 高频题 + 进阶追问
├── tracks/     # 7 天 / 30 天 / 60 天 / AI Infra 路线
├── practice/   # mock、drill、评分卡、复盘
├── projects/   # 系统设计案例、AI 编译器项目表达
├── scripts/    # 索引、dashboard、lint
├── tests/      # 对脚本做回归校验
└── data/       # 来源索引、标签、统计产物
```

## 不同方向怎么入手

### 通用后端 / 社招后端

建议顺序：

1. [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
2. [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
3. [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
4. [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)

### 校招 / 算法基础补齐

建议顺序：

1. [算法专题首页](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
2. [算法核心题清单](/Users/wizout/op/interview/questions/algorithm/00-must-know.md)
3. [OS 核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
4. [每日 Drill](/Users/wizout/op/interview/practice/drills/daily-drill.md)

### AI Infra / AI 编译器

建议顺序：

1. [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
2. [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
3. [AI 编译器项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)
4. [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)

## 现在仓库里已经有什么

### 学习框架

- `Start Here` 入口页
- 五个方向的专题首页
- 角色入口和公司关注点
- 7 天 / 30 天 / 60 天训练路径

### 核心内容

- 五个方向的总览与专题深挖
- 五份“核心题清单”
- 高频题 + 进阶追问
- 系统设计与 AI runtime 案例
- AI 编译器项目表达稿

### 训练闭环

- mock 面试
- 评分卡
- 每日 drill
- 周复盘 / 月复盘

## 最重要的几个入口文件

- [docs/START-HERE.md](/Users/wizout/op/interview/docs/START-HERE.md)
- [docs/guides/repo-map.md](/Users/wizout/op/interview/docs/guides/repo-map.md)
- [docs/guides/review-checklists.md](/Users/wizout/op/interview/docs/guides/review-checklists.md)
- [practice/drills/7-day-rescue-plan.md](/Users/wizout/op/interview/practice/drills/7-day-rescue-plan.md)
- [tracks/sprint-30d/day-by-day.md](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)

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
