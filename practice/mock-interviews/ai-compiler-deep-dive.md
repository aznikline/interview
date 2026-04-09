# Mock 4：AI 编译器深挖

## 场景设定

候选人目标岗位为 AI 编译器 / 推理优化 / 加速库工程。

## 问题序列

1. 为什么 AI 编译器喜欢多级 IR？
2. dynamic shape 为什么麻烦？
3. layout propagation 和 fusion 有什么关系？
4. Triton 为什么适合写某些定制 kernel？
5. 编译器优化和 runtime 调度应该如何分工？
6. 如果某个 fused kernel 平均性能更高，但 P99 更差，你怎么判断要不要上？

## 追问脚本

- 哪些优化必须在 compile time 做？
- 哪些决策应该留到 runtime？
- 你如何验证一个 kernel 真正变快了？

## 评分维度

- 是否有层次感
- 是否理解 hardware-aware optimization
- 是否能围绕指标和 workload 说清楚取舍

## 参考答案

优先按 `IR -> pass -> kernel -> runtime -> metrics` 的顺序组织，不要平铺概念名词。

