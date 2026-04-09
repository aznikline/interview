# 操作系统专题首页

## 1 分钟速答

操作系统在面试里的价值不是考定义，而是解释性能、并发、内存和 I/O 问题。你要能把 OS 概念映射到后端服务里的真实现象。

## 核心机制

### 推荐学习顺序

1. 进程、线程、调度
2. 虚拟内存、页表、TLB
3. I/O、多路复用、零拷贝
4. 锁、并发、内存序

### 必读文档

- [01-os-core.md](/Users/wizout/op/interview/docs/topics/operating-system/01-os-core.md)
- [02-memory-and-io.md](/Users/wizout/op/interview/docs/topics/operating-system/02-memory-and-io.md)
- [03-concurrency-and-scheduling.md](/Users/wizout/op/interview/docs/topics/operating-system/03-concurrency-and-scheduling.md)

## 高频问法

- 进程和线程区别是什么？
- epoll 为什么适合高并发？
- 线程切换为什么贵？
- false sharing 是什么？

## 深挖与误区

- 不能只背概念
- 不能只说“协程更轻量”
- 必须能落到缓存抖动、锁竞争、上下文切换等真实问题

## 下一步

- 刷 [OS 核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- 配合 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md) 一起练

