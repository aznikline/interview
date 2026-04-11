# 训练系统与 Serving

## 1 分钟速答

AI Infra 题最后都会落回系统工程：训练阶段怎么看吞吐和显存，Serving 阶段怎么看 TTFT、TPOT、P99 和稳定性，恢复阶段怎么看放量和资源保护。

## 核心机制

### 训练高频点

- gradient checkpointing
- mixed precision
- 显存复用
- 数据加载和流水线饱和

### Serving 高频点

- prefill / decode
- KV Cache 管理
- dynamic batching
- admission control
- 资源隔离与恢复

## 高频问法

- 显存优化常见手段有哪些？
- 为什么 decode 常 memory bound？
- dynamic batching 为什么有用但危险？
- 推理服务恢复时为什么容易再次抖动？

## 深挖与误区

- 不要只讲训练或只讲推理
- 不要只看平均吞吐，不看 P99 和稳定性
- 不要把系统指标和底层资源割裂开
