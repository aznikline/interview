# Interview Engineering Repo

这是一个面向 `通用后端八股 + 算法 + 系统设计 + 操作系统 + AI 编译器` 的系统化面试工程。

它现在的目标不是“收集资料”，而是尽量接近一套在线教程的使用体验：

- 第一次进入仓库，知道 `先看什么`
- 按你的方向，知道 `下一步学什么`
- 按你的时间，知道 `这一周该怎么安排`
- 学完一篇文档后，知道 `要输出什么`

## 第一次使用，按这个顺序

1. 看 [Start Here](/Users/wizout/op/interview/docs/START-HERE.md)
2. 看 [学习指南](/Users/wizout/op/interview/docs/guides/study-guide.md)
3. 看 [总路线图](/Users/wizout/op/interview/docs/roadmap/00-overview.md)
4. 进入你的方向首页
5. 刷对应方向的核心题清单
6. 执行对应时间线的训练计划

## 如果你现在时间很少

### 只有 3 天

直接看 [学习指南](/Users/wizout/op/interview/docs/guides/study-guide.md) 里的 `3 天版本`，按“后端/OS -> 系统设计/算法 -> AI 编译器/项目表达”推进。

### 只有 1 周

直接执行 [7 天急救计划](/Users/wizout/op/interview/practice/drills/7-day-rescue-plan.md)。

### 有 1 个月

直接执行 [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)。

### 有 2 个月

从 [60 天路径](/Users/wizout/op/interview/tracks/sprint-60d/README.md) 开始，再按方向深化。

## 不同方向怎么入手

### 通用后端 / 社招后端

1. [后端专题首页](/Users/wizout/op/interview/docs/topics/backend/00-index.md)
2. [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
3. [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
4. [系统设计答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-system-design.md)
5. [资深后端 Mock](/Users/wizout/op/interview/practice/mock-interviews/senior-backend.md)

### 校招 / 算法基础补齐

1. [算法专题首页](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
2. [算法框架与训练法](/Users/wizout/op/interview/docs/topics/algorithm/03-frameworks-and-drills.md)
3. [算法核心题清单](/Users/wizout/op/interview/questions/algorithm/00-must-know.md)
4. [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
5. [每日 Drill](/Users/wizout/op/interview/practice/drills/daily-drill.md)

### AI Infra / AI 编译器

1. [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
2. [AI 编译器入门章节](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
3. [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
4. [AI 编译器答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-ai-compiler-interview.md)
5. [AI 编译器项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)

## 仓库是怎么组织的

```text
interview/
├── docs/       # 入口页、路线图、专题教程、答题方法
├── questions/  # 核心题清单、高频题、进阶追问
├── tracks/     # 7 天、30 天、60 天、AI Infra 路线
├── practice/   # mock、drill、评分卡、复盘
├── projects/   # 系统设计案例、项目表达、AI runtime 案例
├── scripts/    # 索引、dashboard、lint、来源同步
├── tests/      # 脚本测试
└── data/       # 来源索引、标签、统计结果
```

它对应的是一套固定的学习闭环：

1. `docs/topics` 建立知识框架
2. `questions` 训练高频问题回答
3. `practice` 做口述输出、mock、复盘
4. `projects` 把知识点变成项目表达

## 先看哪些文件最有效

- [docs/START-HERE.md](/Users/wizout/op/interview/docs/START-HERE.md)
- [docs/guides/study-guide.md](/Users/wizout/op/interview/docs/guides/study-guide.md)
- [docs/guides/repo-map.md](/Users/wizout/op/interview/docs/guides/repo-map.md)
- [docs/guides/review-checklists.md](/Users/wizout/op/interview/docs/guides/review-checklists.md)
- [tracks/sprint-30d/day-by-day.md](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)

## 这次改版参考了哪些在线教程结构

这次入口和内容组织，明确参考了几类成熟教程的结构，不再按“资料堆”来写：

- [roadmap.sh Get Started](https://roadmap.sh/get-started) 和 [Backend Roadmap](https://roadmap.sh/backend)
  参考它的 `角色入口 + 路线图导航`
- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)
  参考它的 `学习顺序 + 高频题 + 系统设计答题法`
- [labuladong 算法小抄](https://labuladong.online/zh/algo/home/)
  参考它的 `理论 -> 框架 -> 例题 -> 练习`
- [MLIR Getting Started](https://mlir.llvm.org/getting_started/) 和 [Toy Tutorial](https://mlir.llvm.org/docs/Tutorials/Toy/)
  参考它的 `前置要求 -> 章节化入门 -> 从 IR 到 lowering 的教程感`

仓库里对应的落地说明见 [在线教程结构参考](/Users/wizout/op/interview/docs/guides/online-tutorial-patterns.md)。

## 内容标准

- 每个专题文档都包含：`1 分钟速答`、`核心机制`、`高频问法`、`深挖与误区`
- 每道题都包含：`题目`、`一句话回答`、`展开回答`、`面试官追问`
- 每个训练路线都尽量给出：`今天看什么`、`今天练什么`、`今天输出什么`
- 每个系统设计案例都覆盖：`需求澄清`、`容量估算`、`核心链路`、`瓶颈与 trade-off`
- AI 编译器部分同时覆盖：`IR`、`lowering`、`fusion`、`runtime`、`性能指标`

## 数据来源策略

仓库正文以 `统一重写和抽象` 为主，不直接复制外部内容。

- GitHub 面经和知识库用于建立题源与主题索引
- 官方文档与官方仓库用于 AI 编译器一手信息
- 微信文章与零散面经只作为问题池补充

来源总表见 [data/sources/source-index.md](/Users/wizout/op/interview/data/sources/source-index.md)。

## 本地维护

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

CI 配置在 [ci.yml](/Users/wizout/op/interview/.github/workflows/ci.yml)。
