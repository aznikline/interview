# CUDA 与 GPU 基础

## 1 分钟速答

CUDA 面试的核心不是会不会写核函数，而是你能不能解释 GPU 是如何靠大量线程、分层内存和 SIMT 执行模型把吞吐做上去，又为什么这些机制会让优化变得敏感。

## 核心机制

### 高频概念

- thread / warp / block / grid
- SM、register、shared memory、global memory
- memory coalescing、bank conflict
- occupancy、latency hiding

### 为什么 kernel 会慢

- 访存不连续
- branch divergence
- occupancy 低
- register 压力高
- kernel launch 开销明显

## 高频问法

- warp 是什么？
- occupancy 高是不是一定更快？
- shared memory 什么时候值得用？
- memory coalescing 为什么重要？

## 深挖与误区

- 不要把 occupancy 当银弹
- 不要只看算力，不看内存带宽
- 不要只会背层级，不会讲性能后果
