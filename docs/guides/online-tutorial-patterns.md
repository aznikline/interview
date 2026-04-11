# 在线教程结构参考

这份仓库改版不是凭感觉写的，而是明确参考了几类成熟教程/知识站的组织方式，然后做成本仓库的 Markdown 版本。

## 参考 1：roadmap.sh

参考链接：

- [Get Started](https://roadmap.sh/get-started)
- [Backend Roadmap](https://roadmap.sh/backend)

借鉴点：

- 先给新用户入口，不让用户先迷失在目录树里
- 先按角色/方向分流，再进入具体知识点
- 路线图的作用是定顺序，不是堆链接

在本仓库里的落地：

- [Start Here](../START-HERE.md)
- [学习指南](study-guide.md)
- 五个方向的 `00-index`

## 参考 2：system-design-primer

参考链接：

- [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

借鉴点：

- 不只给知识点，还给学习顺序和高频问题池
- 系统设计不是散点，而是“如何回答一题”的方法论
- 用案例把抽象概念落下来

在本仓库里的落地：

- [系统设计答题法](how-to-approach-system-design.md)
- [系统设计核心题清单](../../questions/system-design/00-must-know.md)
- [系统设计案例](../../projects/design-case-studies/seckill-system.md)

## 参考 3：labuladong

参考链接：

- [算法小抄首页](https://labuladong.online/zh/algo/home/)

借鉴点：

- 算法内容不是按题号堆，而是按“模板、框架、模式识别”组织
- 理论、例题、练习之间必须能切换
- 目标不是会做，而是会讲和会迁移

在本仓库里的落地：

- [算法专题首页](../topics/algorithm/00-index.md)
- [算法框架与训练法](../topics/algorithm/03-frameworks-and-drills.md)
- [算法核心题清单](../../questions/algorithm/00-must-know.md)

## 参考 4：MLIR Getting Started / Toy Tutorial

参考链接：

- [MLIR Getting Started](https://mlir.llvm.org/getting_started/)
- [Toy Tutorial](https://mlir.llvm.org/docs/Tutorials/Toy/)

借鉴点：

- 高门槛主题必须给“前置条件”和“章节化入门”
- 章节之间要有明显的推进关系：先看整体，再看 IR，再看 lowering，再看 codegen/runtime
- 用户需要一个能按章推进的学习入口，而不是直接扔一堆官方术语

在本仓库里的落地：

- [AI 编译器专题首页](../topics/ai-compiler/00-index.md)
- [AI 编译器入门章节](../topics/ai-compiler/04-getting-started-and-chapters.md)
- [AI 编译器答题法](how-to-approach-ai-compiler-interview.md)

## 改版原则

- 先入口，后内容
- 先顺序，后细节
- 先教程感，后资料堆
- 先输出闭环，后内容扩展
