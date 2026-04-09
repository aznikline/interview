# Interview University

一个面向 `通用后端 + 算法 + 系统设计 + 操作系统 + AI 编译器` 的多月面试学习计划。

这个仓库现在明确按 [coding-interview-university](https://github.com/jwasham/coding-interview-university) 的骨架来组织，不再把自己伪装成“资料目录”。目标很简单：

- 给你一条完整学习路径，而不是一堆零散链接
- 让你知道 `为什么按这个顺序学`
- 让你每天都知道 `看什么、练什么、输出什么`
- 让你从“看过”推进到“能讲、能写、能过面试”

## Table of Contents

- [What Is It](#what-is-it)
- [Why Use It](#why-use-it)
- [How to Use It](#how-to-use-it)
- [Who Is It For](#who-is-it-for)
- [What You Won't See Covered](#what-you-wont-see-covered)
- [The Daily Plan](#the-daily-plan)
- [The Study Plan](#the-study-plan)
- [Final Review](#final-review)
- [Optional Topics](#optional-topics)
- [Closer To The Interview](#closer-to-the-interview)
- [Repo Structure](#repo-structure)
- [Sources and Inspiration](#sources-and-inspiration)
- [Maintenance](#maintenance)

## What Is It

这是一个偏 `大厂后端 / 基础架构 / AI Infra` 面试的系统化学习计划。

如果说 `coding-interview-university` 解决的是“从 web developer 补齐 CS 基础去冲 SDE”，那这个仓库解决的是另一类问题：

- 你已经会写业务，但面试知识体系是碎的
- 你刷过题，但算法、OS、系统设计、项目表达没有串成闭环
- 你想准备后端面试，但不知道 AI 编译器这种差异化方向应该怎么纳入主线

这里不是单纯的题库，也不是单纯的知识库，而是一个 `课程型仓库`：

1. 主入口给出完整学习顺序
2. 每个阶段给出主题、题单、训练输出
3. 最后用 mock、项目表达、复盘把知识变成面试能力

## Why Use It

大多数中文面试仓库的问题不是资料不够，而是：

- 只有目录，没有课程
- 只有题目，没有顺序
- 只有知识点，没有输出要求
- 只有“背什么”，没有“怎么练”

这个仓库要解决的是这些问题：

- 先学什么，后学什么
- 每一阶段的目标是什么
- 看到一篇文档之后，下一步是刷题、mock、还是复盘
- 到最后怎么做总复习，而不是临近面试才乱翻

## How to Use It

像用 `coding-interview-university` 一样用这个仓库，而不是把它当普通 README 看完就走。

### 1. 从总学习计划开始

先看 [Interview University 学习计划](/Users/wizout/op/interview/tracks/interview-university/README.md)。

这份文档是仓库真正的主入口，它会告诉你：

- 总共分几个阶段
- 每个阶段为什么存在
- 每个阶段要学哪些主题
- 学完之后要完成什么输出

### 2. 按阶段推进，不要跳着看

建议顺序：

1. 基础准备
2. 后端主链路
3. 算法与数据结构模式
4. 操作系统与并发
5. 系统设计与分布式取舍
6. AI 编译器差异化专题
7. 最终复习与 mock

### 3. 每完成一个主题就做输出

只看文档没有意义。至少做一个动作：

- 口述 `1 分钟回答`
- 刷对应题单
- 做一次 mock
- 更新你的弱项清单

### 4. 用 checklist 管进度

这个仓库现在推荐你直接在课程文档里打勾推进，就像 `coding-interview-university` 那样维护自己的学习状态。

## Who Is It For

- 准备 `通用后端` 面试的人
- 准备 `中高级后端 / 基础架构 / 分布式` 面试的人
- 想系统补 `算法 + OS + 系统设计` 的人
- 想把 `AI Infra / AI 编译器 / 推理优化` 当作差异化加分项的人

## What You Won't See Covered

这些内容很常见，但不是这份学习计划的主线：

- 前端框架细节
- HTML / CSS / 浏览器工程化
- Android / iOS 专项
- DevOps 全量技能树
- 完整机器学习训练体系

这不代表它们不重要，只是这份仓库的目标是后端和基础设施面试，而不是覆盖所有岗位。

## The Daily Plan

有些主题一天能过完，有些主题会持续几天。一个推荐的日计划如下：

### 每天固定三段

1. 学习主题
2. 刷题或口述输出
3. 复盘和记录弱项

### 每天最低输出

- 说清 `1 个主题` 的 1 分钟回答
- 刷 `2-5` 个对应问题
- 记录 `1-3` 个不会答或答不稳的点

### 每周最低输出

- `1` 次 mock
- `1` 次周复盘
- `1` 份项目表达修订

如果你只剩一周时间，看 [7 天急救计划](/Users/wizout/op/interview/practice/drills/7-day-rescue-plan.md)。

如果你还有一个月，直接执行 [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)。

## The Study Plan

完整课程在这里：

- [Interview University 学习计划](/Users/wizout/op/interview/tracks/interview-university/README.md)
- [Optional Topics](/Users/wizout/op/interview/tracks/interview-university/optional-topics.md)

它是这套仓库的核心，总共分成 7 个阶段：

### 0. Before You Start

- 明确目标岗位
- 明确时间预算
- 明确主语言和主方向

### 1. Backend Core

- MySQL
- Redis
- MQ
- 一致性、幂等、限流、降级

### 2. Algorithms and Data Structures

- 模式识别
- 模板化表达
- 高频题训练

### 3. Operating Systems and Concurrency

- 进程线程
- 内存
- I/O
- 调度
- 锁与并发

### 4. System Design

- 容量估算
- 缓存
- 高并发
- 数据一致性
- trade-off

### 5. AI Compiler and AI Infra

- IR
- lowering
- fusion
- runtime
- 性能指标

### 6. Final Review

- mock
- 项目表达
- 弱项复盘
- 总冲刺

## Final Review

总复习入口放在这里：

- [Final Review Checklist](/Users/wizout/op/interview/tracks/interview-university/final-review.md)

这个阶段不是继续扩知识面，而是做四件事：

- 把高频题讲顺
- 把系统设计讲成有结构的答案
- 把项目故事讲成“问题-方案-取舍-指标”
- 把 AI 编译器专题讲成完整链路，而不是术语堆

## Optional Topics

如果你时间充足，或者目标是更偏基础设施/平台岗位，可以追加这些专题：

- 计算机网络
- Linux 工具链
- 搜索与索引
- 更深入的数据库内部机制
- 编译原理基础
- runtime 调度
- 消息、序列化、队列系统

这些内容后面可以继续扩，但不会先于主线阶段。

详细列表见 [Optional Topics](/Users/wizout/op/interview/tracks/interview-university/optional-topics.md)。

## Closer To The Interview

如果你已经进入投递或面试周，不要继续漫无目的扩资料，直接切到：

- [Final Review Checklist](/Users/wizout/op/interview/tracks/interview-university/final-review.md)
- [Closer To The Interview](/Users/wizout/op/interview/tracks/interview-university/closer-to-interview.md)
- [30 天逐日执行表](/Users/wizout/op/interview/tracks/sprint-30d/day-by-day.md)

这个阶段最重要的不是再学新知识，而是：

- 把高频题讲顺
- 把项目故事讲稳
- 把系统设计答题结构固定下来
- 明确弱项，只做针对性修补

## Repo Structure

```text
interview/
├── README.md
├── docs/
│   ├── START-HERE.md
│   ├── roadmap/
│   ├── guides/
│   └── topics/
├── questions/
├── tracks/
│   ├── interview-university/
│   ├── sprint-30d/
│   └── sprint-60d/
├── practice/
├── projects/
├── scripts/
├── tests/
└── data/
```

仓库里的职责分工：

- `tracks/interview-university` 负责完整课程主线
- `docs/topics` 负责系统化讲解
- `questions` 负责高频问题训练
- `practice` 负责 mock、drill、复盘
- `projects` 负责项目表达与案例

## Sources and Inspiration

这次重构明确参考了这些仓库和文档：

- [coding-interview-university](https://github.com/jwasham/coding-interview-university)
- [system-design-primer](https://github.com/donnemartin/system-design-primer)
- [roadmap.sh Backend](https://roadmap.sh/backend)
- [labuladong 算法小抄](https://labuladong.online/zh/algo/home/)
- [MLIR Getting Started](https://mlir.llvm.org/getting_started/)
- [MLIR Toy Tutorial](https://mlir.llvm.org/docs/Tutorials/Toy/)

来源索引见 [data/sources/source-index.md](/Users/wizout/op/interview/data/sources/source-index.md)。

## Maintenance

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
