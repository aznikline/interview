# AI 编译器核心题清单

## 题目

AI 编译器面试最该优先准备哪些问题，准备顺序应该怎么排？

## 一句话回答

优先准备能把链路讲完整的问题：`模型/图 -> IR -> lowering -> fusion -> kernel -> runtime -> 指标`。顺序上先讲整体框架，再补细节深挖，再把问题落到项目和性能收益。

## 展开回答

### 第一层：必须先拿下的 10 题

- AI 编译器和传统编译器最大区别是什么？
- MLIR、XLA、TVM、Triton 分别解决什么问题？
- 为什么要多级 IR？
- lowering 在做什么？
- 算子融合为什么能提速？
- layout 为什么会影响性能？
- 动态 shape 为什么难？
- 编译器和 runtime 怎么分工？
- 为什么 decode 阶段常常 memory bound？
- 如何评估一个优化真的有效？

### 第二层：必须会说的指标

这些指标要能解释“为什么变好”：

- TTFT
- TPOT
- throughput
- P99 latency
- memory footprint
- kernel launch overhead

### 第三层：必须能接住的深挖

- 融合为什么可能变慢？
- layout change 为什么会影响访存效率？
- runtime 为什么不能完全替代编译优化？
- Triton 和 CUDA 的关系是什么？
- KV cache、batching、动态 shape 为什么会把 runtime 拉进来？

### 建议刷题顺序

1. 先看 [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
2. 再看 [AI 编译器入门章节](/Users/wizout/op/interview/docs/topics/ai-compiler/04-getting-started-and-chapters.md)
3. 然后刷 [AI 编译器高频题](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
4. 再刷 [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
5. 最后看 [项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)

### 每题最低输出标准

每道题至少要能说出：

- 这题属于链路中的哪一层
- 它解决了什么瓶颈
- 它和 runtime 或硬件有什么关系
- 它最终影响了哪个指标

### 1 分钟速答表

| 题目 | 最低合格回答 |
| --- | --- |
| AI 编译器和传统编译器最大区别是什么？ | 前者更强依赖张量算子、硬件特性和 runtime 协同，目标通常不是“能跑”而是“更快更省”。 |
| 为什么要多级 IR？ | 因为不同层级要表达的问题不同，高层更适合图优化，低层更适合贴近 kernel 和硬件。 |
| lowering 在做什么？ | 它把高层抽象逐步降到更具体的表示，核心是把优化空间转成可执行实现。 |
| 算子融合为什么能提速？ | 通常因为减少中间结果读写、kernel launch 和访存开销，但融合过头也可能让调度更差。 |
| layout 为什么影响性能？ | 因为数据排布直接决定访存连续性、cache 命中和向量化效率。 |
| 动态 shape 为什么难？ | 它会压缩静态优化空间，增加 shape 推断、kernel 选择和 runtime 调度复杂度。 |
| 编译器和 runtime 怎么分工？ | 编译器更擅长提前做结构和算子层优化，runtime 更擅长根据在线输入、batch 和资源做决策。 |
| decode 为什么常 memory bound？ | 因为每步计算量相对小，但 KV cache 访问和内存带宽压力很高。 |
| 怎么证明优化真的有效？ | 不能只看平均耗时，要结合 TTFT、TPOT、throughput、P99 和 memory footprint 看是否真实受益。 |
| Triton、TVM、XLA、MLIR 该怎么区分？ | 它们关注层级和定位不同，面试里重点是说清谁在 IR、谁在 codegen、谁更偏框架或 runtime 协同。 |

### 最小合格回答标准

如果你没有完整 compiler 项目经历，最低也要做到：

- 每题都能明确它在 `图 / IR / kernel / runtime` 链路中的位置
- 能说清一个性能瓶颈，而不是只背框架名
- 能把答案落到一个指标，比如 TTFT、TPOT、吞吐或显存
- 被追问时至少能继续讲 `为什么难 / 为什么没选另一种做法`

## 面试官追问

- 如果只给你 30 分钟准备，你先讲哪 5 题？
- 哪些题最适合连到 LLM 推理优化？
- 哪些题最容易被追问到底层实现？
- 如果没有完整 compiler 项目经历，怎么把这套题讲得可信？

## 易错点

- 只会背框架名
- 不会讲层次边界
- 不会把问题落到 runtime 和服务侧
- 不会用指标证明收益

## 关联知识点

- [AI 编译器专题首页](/Users/wizout/op/interview/docs/topics/ai-compiler/00-index.md)
- [AI 编译器高频题](/Users/wizout/op/interview/questions/ai-compiler/high-frequency.md)
- [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- [AI 编译器答题法](/Users/wizout/op/interview/docs/guides/how-to-approach-ai-compiler-interview.md)
- [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
