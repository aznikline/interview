# Optional Topics

这些内容不是主线必修，但会显著提高你在基础设施岗位上的上限。

## 什么时候该学 Optional Topics

适合这几类情况：

- 你主线已经走完一轮
- 你目标岗位更偏平台 / 基础设施 / 中间件
- 你需要在简历或项目之外建立差异化

如果主线还没走完，不要拿 optional topics 逃避主线短板。

## Topic 1: 网络与协议

为什么值得补：

- 后端和系统设计经常会追问 TCP、拥塞、重传、连接管理
- 网络基础能帮助你理解尾延迟、超时、负载均衡和慢请求

建议重点：

- TCP 三次握手 / 四次挥手
- TIME_WAIT / CLOSE_WAIT
- 粘包拆包
- 重传、流量控制、拥塞控制
- HTTP/1.1、HTTP/2、HTTP/3 的差异

建议入口：

- [网络与协议基础](/Users/wizout/op/interview/docs/topics/backend/05-network-and-protocols.md)

## Topic 2: 搜索与索引

为什么值得补：

- 搜索、推荐、广告和内容平台岗位常会问检索和倒排
- 系统设计里的搜索建议、召回、分页和排序都和索引有关

建议重点：

- 倒排索引
- 分词和查询解析
- 分页与排序
- 实时索引与离线构建

建议入口：

- [搜索、索引与消息系统设计](/Users/wizout/op/interview/docs/topics/system-design/04-search-and-messaging.md)

## Topic 3: 更深入的数据库内部机制

为什么值得补：

- 中高级后端经常会把问题从“会用数据库”追到“理解数据库如何工作”

建议重点：

- B+ 树页结构
- redo/undo/binlog
- checkpoint
- flush 与 fsync
- 锁和隔离级别实现

## Topic 4: 消息、序列化与队列系统

为什么值得补：

- MQ 已经是后端主线的一部分，但更深入的消息系统设计会拉开资深度差距

建议重点：

- push / pull 模型
- offset 与消费组
- 顺序消息
- 死信队列
- 序列化格式与兼容性

## Topic 5: 编译原理基础

为什么值得补：

- 对 AI 编译器方向来说，编译原理基础会决定你能不能真正理解 IR、pass 和 lowering

建议重点：

- AST、IR、CFG
- SSA
- dataflow analysis
- 指令选择、寄存器分配的基本概念

## Topic 6: Linux 工具链与排障

为什么值得补：

- 面试里很容易追问“线上怎么排”
- 这是把 OS、网络、性能问题落到工程实践的关键

建议重点：

- top / htop / ps
- vmstat / iostat / sar
- strace / ltrace
- perf / flame graph
- netstat / ss / lsof

建议入口：

- [Linux 可观测性与性能排障](/Users/wizout/op/interview/docs/topics/operating-system/04-linux-observability-and-tuning.md)

## Topic 7: Runtime 调度与 Serving

为什么值得补：

- AI Infra 和大模型推理岗位越来越常问 runtime 层问题

建议重点：

- dynamic batching
- KV cache 管理
- prefill / decode 分离
- scheduler 与 admission control
- TTFT / TPOT / throughput 的 trade-off

建议入口：

- [Serving Runtime 与在线调度](/Users/wizout/op/interview/docs/topics/ai-compiler/05-serving-and-runtime-systems.md)

## 学 Optional Topics 的顺序建议

### 如果你偏后端 / 基础架构

1. 网络与协议
2. 更深入的数据库内部机制
3. 消息、序列化与队列系统
4. Linux 工具链与排障

### 如果你偏 AI Infra / AI 编译器

1. 编译原理基础
2. Runtime 调度与 Serving
3. Linux 工具链与排障
4. 网络与协议
