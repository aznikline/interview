# IR、Lowering 与 Dialect

## 1 分钟速答

AI 编译器之所以绕不开 IR，是因为模型表示、优化规则和后端硬件天然分层。IR 让前端框架、优化 passes 和硬件代码生成解耦，而 lowering 则是把高层张量语义逐步映射到更接近硬件执行的表示。

## 核心机制

### 为什么需要多层 IR

- 高层 IR 便于表达图结构和张量语义
- 中层 IR 便于做融合、shape 推导和布局变换
- 低层 IR 便于映射线程块、向量化和内存层级

### MLIR / Dialect 思想

- 不同层级用不同 dialect 描述语义
- 通过 pass pipeline 完成 canonicalization、bufferization、conversion
- Dialect conversion 是面试高频关键词

### Lowering 的意义

- 从“算什么”走向“怎么在设备上算”
- 把抽象操作拆成更接近 kernel 的形式
- 逐步暴露布局、线程映射、内存规划

## 高频问法

- 为什么 AI 编译器喜欢多级 IR，而不是单一 IR？
- dialect 和 pass 分别解决什么问题？
- lowering 过程中 shape 信息为什么关键？

## 深挖与误区

- IR 不是越多越好，层级过多会增加维护成本
- lowering 不只是“翻译语法”，而是逐步引入实现细节
- 面试里要讲“信息何时暴露、为什么此时暴露”

