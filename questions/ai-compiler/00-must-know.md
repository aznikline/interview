# AI 编译器核心题清单

## 题目

AI 编译器面试最该优先准备哪些问题？

## 一句话回答

优先准备能把编译器链路讲完整的问题：IR、lowering、fusion、layout、kernel、runtime、动态 shape、性能指标、LLM 推理优化。

## 展开回答

### 第一优先级：必须会讲

- AI 编译器和传统编译器最大区别是什么？
- MLIR、XLA、TVM、Triton 分别解决什么问题？
- 为什么要多级 IR？
- lowering 在做什么？
- 算子融合为什么能提速？
- layout 为什么影响性能？
- 动态 shape 为什么难？
- 编译器和 runtime 怎么分工？
- 为什么 decode 阶段常常 memory bound？
- 如何评估一个优化真的有效？

### 必须会说的指标

- TTFT
- TPOT
- throughput
- P99 latency
- memory footprint
- kernel launch overhead

## 面试官追问

- 融合为什么可能变慢？
- runtime 为什么不能完全替代编译优化？
- Triton 和 CUDA 的关系是什么？

## 易错点

- 只会背框架名
- 不会讲层次边界
- 不会用指标证明收益

## 关联知识点

- [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [AI 编译器高频题](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
- [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)

