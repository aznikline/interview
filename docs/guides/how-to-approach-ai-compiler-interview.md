# AI 编译器答题法

AI 编译器面试最容易答崩的原因，不是不会某个框架，而是答题没有层次。正确的方式不是从“我用过 TVM/MLIR”开始，而是从完整链路开始。

## 一套稳定的五层答法

### 1. 模型和图层

先说明优化对象是什么：

- 是训练还是推理
- 是 CNN、Transformer 还是 LLM serving
- 图是静态还是动态
- 主要瓶颈是算力、带宽还是调度

没有这个前提，后面的 compiler/runtime 讨论会漂。

### 2. IR 和编译层

再讲为什么需要 IR：

- 不同前端模型如何统一表示
- 为什么需要多级 IR
- lowering 在做什么
- 哪些优化适合放在 compile time

这一层要能讲清 `graph IR / dialect / pass / legality` 这些基本概念。

### 3. Kernel 和算子层

再往下讲：

- 哪些算子适合融合
- 为什么 layout 会影响性能
- memory access pattern 如何决定效率
- Triton / CUDA / codegen 在这里分别扮演什么角色

如果这一层说不清，面试官会判断你只是“框架使用者”。

### 4. Runtime 层

很多人只讲编译器，不讲 runtime，这是明显短板。要补这些问题：

- 编译结果如何被 runtime 调度
- 动态 batch、KV cache、streaming decode 怎么影响 runtime
- 编译器和 runtime 的边界在哪里
- 在线服务里哪些决策必须在 runtime 才能做

### 5. 指标层

最后一定要落到指标，不然优化收益无法自证：

- TTFT
- TPOT
- throughput
- P99 latency
- memory footprint

优化不是“感觉快了”，而是“哪个指标为什么改善了”。

## 一个 1 分钟回答模板

如果被问“你怎么理解 AI 编译器链路”，可以按这个顺序答：

先明确模型和目标场景，再讲前端图如何落到多级 IR，接着讲 lowering、fusion、layout 和 codegen 如何把高层语义变成高效 kernel，最后讲 runtime 如何承接动态 shape、batching 和在线调度，并用 TTFT、TPOT、吞吐和显存占用去验证优化是否有效。

## 高频追问怎么接

### 动态 shape 为什么难

因为编译期很多假设不再稳定，shape 推导、buffer planning、kernel 选择和合法性检查都会更复杂，部分优化必须推迟到 runtime。

### 算子融合为什么可能变慢

融合会减少中间访存和 launch overhead，但也可能带来寄存器压力、occupancy 下降、调优空间缩小，所以不是融合越多越好。

### runtime 为什么不能完全替代编译器

runtime 更适合做在线决策和动态调度，但很多全局静态优化，比如跨算子重写、IR 级别合法变换、代码生成，仍然需要编译期完成。

## 最常见的错误

- 只背框架名，不讲链路
- 只讲 compiler，不讲 runtime
- 只讲概念，不讲指标
- 说自己做了优化，但说不出瓶颈定位方法

## 推荐结合仓库里的这些内容一起看

- [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [AI 编译器入门章节](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
- [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- [LLM 推理编译案例](/Users/wizout/op/interview/projects/ai-compiler-case-studies/llm-inference-compiler.md)
