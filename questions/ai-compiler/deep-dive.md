# AI 编译器进阶题

## 题目

为什么动态 shape 会让 AI 编译器更难优化？

## 一句话回答

因为很多静态优化都依赖已知 shape，例如内存规划、布局选择、kernel 特化和融合边界；一旦 shape 运行时才确定，编译器就需要保守处理或把决策下沉到 runtime。

## 展开回答

- 静态 shape 下可以提前做 buffer planning 和特化代码生成
- 动态 shape 让某些 fusion 或 tile 策略失去确定性
- runtime 可能需要缓存多个编译产物或做 JIT / fallback
- LLM 服务里的 batch 变化和序列长度变化都属于这类问题

## 面试官追问

- 动态 shape 下哪些优化最容易退化？
- shape polymorphism 怎么理解？
- runtime 如何补足编译期信息不足？

---

## 题目

为什么 AI 编译器里要关注 layout？

## 一句话回答

因为张量布局直接决定访存连续性、向量化方式和 kernel 实现成本，同一算子在不同 layout 下性能可能差很多。

## 展开回答

- layout 会影响 coalesced memory access
- 某些 fused kernel 对特定 layout 更友好
- layout 转换本身有成本，不能无限切换
- 编译器要在算子局部最优和全局链路代价之间取舍

## 面试官追问

- NHWC 和 NCHW 切换的成本体现在哪里？
- layout propagation 为什么重要？
- 为什么 layout 优化要和 fusion 一起看？

---

## 题目

Triton 为什么在 AI Infra 面试里常出现？

## 一句话回答

因为 Triton 处在“高层易写”和“底层可控”之间，适合展示你对 GPU kernel、autotuning 和编译器抽象边界的理解。

## 展开回答

- Triton 提供 Python 风格 kernel 编写方式
- 底层仍暴露 block、warp、pipeline 等性能关键参数
- 很多推理优化实践会用 Triton 写定制 kernel
- 它还能引出 Triton IR / MLIR、autotune、layout 和 tensor core 使用

## 面试官追问

- Triton 和 CUDA 各自适合什么场景？
- Triton 的 autotune 在做什么？
- 什么样的 kernel 不适合用 Triton？

---

## 题目

编译器优化和 runtime 调度冲突时，你怎么取舍？

## 一句话回答

要先看目标函数是吞吐、延迟还是成本，然后判断问题更偏静态结构还是动态执行环境；编译器负责结构性优化，runtime 负责在线决策，冲突时应围绕指标做分层分工。

## 展开回答

- 编译器擅长固定图结构与目标代码生成
- runtime 擅长动态 batch、资源占用、在线负载变化
- 低延迟服务可能更保守，避免过度特化
- 离线批处理可能更激进，优先吞吐

## 面试官追问

- 如何验证一个优化该放在哪层？
- 什么时候需要多版本编译产物？
- P99 延迟和吞吐冲突时你怎么选？

