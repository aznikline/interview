# AI 编译器入门与章节推进

## 1 分钟速答

AI 编译器不适合“从术语堆开始学”。更稳定的入门方式是按章节推进：先确认前置条件，再看整体链路，再进入 IR、lowering、fusion、runtime，最后回到项目表达和性能指标。

## 核心机制

### 第 0 章：前置条件

在进入 AI 编译器之前，最好先补这些前置：

- 线性代数和张量基础
- GPU 执行模型和显存层次
- 基本编译原理概念：IR、pass、合法变换
- LLM 推理链路常识：prefill、decode、KV cache

如果这些前置缺得太多，直接看 compiler 细节会非常碎。

### 第 1 章：整体链路

先搞清一条完整链路：

模型前端 -> 图表示 -> IR -> lowering -> 优化 -> codegen -> runtime -> 指标验证

这一步的目标不是深挖某个框架，而是知道每一层的职责边界。

### 第 2 章：IR 与 lowering

这一章重点解决：

- 为什么要多级 IR
- dialect 在表达什么
- lowering 是语义收敛还是语义展开
- 合法性和可优化性怎么平衡

### 第 3 章：融合、布局和 kernel

这一章重点解决：

- 融合为什么能降低访存和 launch overhead
- 为什么 layout 变化会影响吞吐和延迟
- kernel 生成和 autotune 的边界在哪里

### 第 4 章：runtime 与在线服务

这一章重点解决：

- 动态 batch 和 streaming decode 为什么把 runtime 拉进来
- compiler 和 runtime 的边界怎么划
- 哪些问题必须在线决策

### 第 5 章：项目表达

最后必须回到面试表达：

- 你解决了什么瓶颈
- 你是怎么定位问题的
- 你做了哪类优化
- 你用什么指标证明收益

这一章决定你能不能把知识点真正转成面试故事。

## 高频问法

- 为什么 AI 编译器需要多级 IR？
- lowering 的本质是什么？
- 动态 shape 为什么对编译器和 runtime 都构成挑战？
- 融合为什么不一定越多越好？
- 在线 serving 里 compiler 和 runtime 怎么协同？

## 深挖与误区

### 误区 1：把 AI 编译器准备成框架名表

只背 MLIR、TVM、XLA、Triton 的名字，没有意义。你必须知道它们在链路里解决的到底是哪一段问题。

### 误区 2：只看编译期，不看运行期

LLM serving 的很多真实瓶颈都和 runtime、batching、KV cache、调度有关，只讲 compiler 会显得视角过窄。

### 误区 3：不会回到指标

面试里最终要回答的是：优化到底带来了什么收益。没有 TTFT、TPOT、吞吐、显存占用这些指标，故事就立不起来。

## 推荐和仓库里的这些内容串起来看

1. [01-ai-compiler-core.md](01-ai-compiler-core.md)
2. [02-ir-lowering-and-dialects.md](02-ir-lowering-and-dialects.md)
3. [03-kernel-fusion-and-runtime.md](03-kernel-fusion-and-runtime.md)
4. [AI 编译器答题法](../../guides/how-to-approach-ai-compiler-interview.md)
5. [AI 编译器项目表达稿](../../../projects/ai-compiler-case-studies/project-storytelling.md)
