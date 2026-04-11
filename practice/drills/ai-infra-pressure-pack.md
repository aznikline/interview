# AI Infra 压测包

适合：

- CUDA / 并行 / 推理服务题会背，但一追问就散
- 想把硬件层和系统层讲成一条线

## 使用方法

- 每次只选 `1` 个主问题
- 主问题答 `1-2` 分钟，再接 `3` 轮追问
- 每轮都回到 `瓶颈 / 资源 / 指标 / trade-off`

## Section 1：CUDA 性能

### 主问题

occupancy 高是不是一定更快？

### 第一轮追问

- latency hiding 在这里扮演什么角色？
- shared memory 和寄存器压力怎么影响它？
- branch divergence 为什么会破坏收益？

### 第二轮追问

- memory coalescing 和 occupancy 谁更重要？
- 为什么低 occupancy 也可能跑得快？
- 如果 kernel 很慢你先看什么？

### 第三轮追问

- 如果面试官继续追问 roofline 和 profiling，你怎么接？
- 如果指标冲突，你先保哪一个？
- 如何一句话解释“occupancy 不是银弹”？

## Section 2：通信与并行

### 主问题

为什么多卡训练往往会被通信拖慢？

### 第一轮追问

- AllReduce 在做什么？
- 拓扑为什么重要？
- 哪类并行更吃通信？

### 第二轮追问

- NVLink 和 PCIe 的差别为什么重要？
- 为什么加卡不等于线性提速？
- 怎么用 overlap 减轻通信成本？

### 第三轮追问

- 如果继续追问 NCCL、流水线 bubble、序列并行，你先讲哪层？
- 如果吞吐不升反降，先看什么指标？
- 如何一句话解释“通信不是附属成本”？

## Section 3：训练与 Serving

### 主问题

为什么 decode 常常 memory bound？

### 第一轮追问

- prefill 和 decode 的代价结构差在哪？
- KV Cache 为什么重要？
- 显存为什么会成为核心约束？

### 第二轮追问

- dynamic batching 为什么有用但危险？
- TTFT、吞吐、P99 如何平衡？
- 恢复期为什么也会再次抖？

### 第三轮追问

- 如果继续追问 admission control、cache 回收和恢复放量，你怎么接？
- 如果线上平均更快但 P99 更差，你怎么判断？
- 如何一句话解释“AI Infra 是系统工程题”？

## 复盘问题

- 我最容易在哪类问题上掉到术语堆砌？
- 我有没有把硬件层和服务层断开？
- 我有没有讲指标和 trade-off？
