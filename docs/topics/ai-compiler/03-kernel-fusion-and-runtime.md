# Kernel 融合与 Runtime 协同

## 1 分钟速答

AI 编译优化不是只靠 compiler pass，也不是只靠 runtime 调度。真正高性能依赖两者协作：编译器决定图变换、kernel 形态和内存布局，runtime 决定执行计划、batch、stream、memory planning 和设备调度。

## 核心机制

### Kernel 融合

- 减少中间张量写回
- 减少 launch overhead
- 改善 locality

### Runtime 协同

- 动态 batch
- 执行流调度
- 内存池与复用
- 编译产物选择与 fallback

### LLM 推理特殊性

- prefill 与 decode 特征不同
- KV cache 影响显存与带宽
- 小 batch 低延迟与大 batch 高吞吐目标不同

## 高频问法

- 为什么 decode 常常更 memory bound？
- runtime 在动态 shape 场景里扮演什么角色？
- 为什么 fused kernel 可能提高吞吐却拉高尾延迟？

## 深挖与误区

- 编译器和 runtime 的边界是协作关系，不是二选一
- 只看平均延迟容易误导，要看 TTFT、TPOT、P99
- 融合过度会放大寄存器和共享内存压力

