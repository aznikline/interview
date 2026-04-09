# Interview Engineering Repo

一个面向 `通用后端八股 + 算法 + 系统设计 + 操作系统 + AI 编译器` 的系统化面试工程。

目标不是堆资料，而是把分散的面经、题库、知识点、项目表达和训练计划，整理成一个可持续迭代的仓库：

- `知识库`：按主题系统化梳理原理、答法、追问和误区
- `训练营`：按题目、计划、模拟面试、周复盘做闭环
- `课程化路线`：按阶段组织学习路径，适配校招、社招、AI infra 方向

## 目录结构

```text
interview/
├── docs/                 # 系统讲解、路线图、指南、模板
├── questions/            # 高频题与标准答法
├── tracks/               # 30 天 / 60 天 / AI Infra 等训练路径
├── practice/             # 模拟面试、drill、复盘
├── projects/             # 讲项目与系统设计案例
├── scripts/              # 索引构建、文档检查、进度面板
├── tests/                # 脚本测试
└── data/                 # 来源、标签、统计产物
```

## 快速开始

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python scripts/build_index.py
python scripts/generate_progress.py
python scripts/lint_docs.py
pytest
```

## 使用方式

1. `先过 roadmap`
确定目标岗位、阶段和优先级。

2. `再过 topics`
先形成结构化理解，不要直接背碎片答案。

3. `然后刷 questions`
每道题先说 1 分钟版，再补展开版和追问版。

4. `最后跑 practice / projects`
把知识点变成可输出、可讲述的面试表达。

## 内容标准

- 每个主题文档都包含：`1 分钟速答`、`核心机制`、`高频问法`、`深挖与误区`
- 每道题都包含：`题目`、`一句话回答`、`展开回答`、`面试官追问`
- 每个系统设计案例都包含：`需求澄清`、`容量估算`、`核心组件`、`瓶颈与 trade-off`
- AI 编译器部分同时覆盖：`图编译`、`算子优化`、`运行时协同`、`硬件适配`

## 当前首版范围

- 后端基础：并发、事务、缓存、MQ、分布式
- 算法：双指针、滑窗、二分、BFS/DFS、DP、回溯、堆、并查集
- 系统设计：短链、消息队列、Feed、秒杀、缓存一致性
- 操作系统：进程线程、内存、I/O、多路复用、锁、调度
- AI 编译器：MLIR / XLA / TVM / Triton / 推理优化基础

## 数据来源策略

仓库内容以 `重新整理和抽象` 为主，不直接复制外部仓库。

- GitHub 面经 / 题库 / CS 知识仓库用于建立题源与专题索引
- 官方文档与官方仓库用于 AI 编译器专题的一手信息
- 微信文章中的题目用于补充初版问题池，已纳入题目组织结构

来源见 [data/sources/source-index.md](/Users/wizout/op/interview/data/sources/source-index.md)。

