# Phase 3: Operating Systems And Concurrency

这个阶段的目标不是背定义，而是把 OS 讲成后端性能和并发现象的解释器。

## 阶段目标

- 能解释线程、内存、I/O、调度这些机制为什么重要
- 能把系统机制连到真实服务的性能问题
- 能用 OS 语言回答“为什么会慢 / 为什么会抖 / 为什么会争用”

## 建议时长

- 标准版：`7-10 天`
- 压缩版：`3-5 天`

## 推荐学习顺序

1. [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
2. [OS 核心](/Users/wizout/op/interview/docs/topics/operating-system/01-os-core.md)
3. [内存与 I/O](/Users/wizout/op/interview/docs/topics/operating-system/02-memory-and-io.md)
4. [并发与调度](/Users/wizout/op/interview/docs/topics/operating-system/03-concurrency-and-scheduling.md)
5. [OS 核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
6. [OS 高频题](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
7. [并发与内存题](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)

## 这阶段必须拿下的核心问题

- 进程和线程区别是什么？
- 上下文切换为什么贵？
- 用户态和内核态如何切换？
- 虚拟内存、页表、TLB 在做什么？
- epoll 为什么适合高并发？
- 零拷贝到底减少了什么开销？
- false sharing、锁竞争、内存屏障分别影响什么？

## 每周输出要求

### 输出 1：现象归因

挑一个典型性能问题，尝试用 OS 机制解释：

- 为什么 CPU 很高
- 为什么延迟长尾
- 为什么吞吐上不去

### 输出 2：题目口述

至少完成 `8-10` 个 OS 高频题的口述，把每题都讲成：

- 它是什么
- 为什么存在
- 它影响了什么工程现象

### 输出 3：和后端联动

把 OS 题和后端主链路里的问题连起来，比如：

- epoll 和网络服务
- zero-copy 和大流量传输
- 锁竞争和热点更新

## 退出条件

- 能稳定解释 `线程 / 内存 / I/O / 锁` 四大类问题
- 不再只会背教材定义
- 至少能把 `3` 个系统机制和线上性能现象连起来

## 这个阶段最容易失败的方式

- 只背定义，不讲代价
- 只会说“协程更轻量”，但说不出轻在哪里
- 把缓存 miss、page fault、上下文切换、锁竞争混成一团
