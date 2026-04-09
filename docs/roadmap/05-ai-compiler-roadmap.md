# AI 编译器路线图

## 为什么单独拉一条线

AI 编译器岗位与普通后端不同，除了系统能力，还要求你理解：

- 计算图表示
- 图优化与 lowering
- kernel / operator 调优
- 编译器和 runtime 的边界
- 硬件后端适配

## 学习顺序

1. 先理解推理链路：模型 -> 图 -> kernel -> runtime -> device
2. 再理解主流栈：MLIR / XLA / TVM / Triton
3. 最后建立面试表达：为什么优化、优化什么、怎么验证收益

