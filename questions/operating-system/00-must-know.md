# 操作系统核心题清单

## 题目

后端面试里的操作系统最该准备哪些题，顺序应该怎么排？

## 一句话回答

优先准备最能解释性能和并发现象的题：`进程线程 -> 上下文切换 -> 虚拟内存 -> I/O 模型 -> 多路复用 -> 零拷贝 -> 锁与内存模型`。顺序上先抓“现象背后的机制”，再抓“和服务性能的关系”。

## 展开回答

### 第一层：必须会讲的基础机制

- 进程和线程区别是什么？
- 线程切换为什么贵？
- 用户态和内核态如何切换？
- 虚拟内存解决了什么问题？
- page fault 为什么会导致抖动？
- select / poll / epoll 区别是什么？
- zero-copy / sendfile / mmap 是什么？
- 死锁为什么发生？如何避免？
- false sharing 是什么？
- 内存屏障为什么重要？

### 第二层：必须能连到工程现象

这些问题不能只背定义，必须能联系到服务问题：

- 为什么高并发服务会被上下文切换拖垮
- 为什么 epoll 服务仍然可能被慢请求拖慢
- 为什么 page fault 和缓存 miss 会放大尾延迟
- 为什么锁竞争和 false sharing 都会让 CPU 很忙但吞吐上不去

### 第三层：建议刷题顺序

1. 先看 [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
2. 再看 [OS 核心](/Users/wizout/op/interview/docs/topics/operating-system/01-os-core.md)
3. 再看 [内存与 I/O](/Users/wizout/op/interview/docs/topics/operating-system/02-memory-and-io.md)
4. 再看 [并发与调度](/Users/wizout/op/interview/docs/topics/operating-system/03-concurrency-and-scheduling.md)
5. 然后刷 [OS 高频题](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
6. 最后刷 [并发与内存题](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)

### 第四层：最小交付标准

每类问题至少要做到：

- 讲清“它是什么”
- 讲清“为什么会有它”
- 讲清“它影响了什么性能或并发现象”
- 讲清“工程里如何观察和缓解”

## 面试官追问

- 为什么 epoll 服务还会被慢请求拖垮？
- 协程为什么不是万能方案？
- 锁竞争和 false sharing 有什么区别？
- page fault、TLB miss、cache miss 谁更贵？
- 零拷贝为什么不是完全零成本？

## 易错点

- 只会教材定义
- 不会结合真实服务
- 不会讲系统层开销
- 把内核机制和业务现象割裂开

## 关联知识点

- [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
- [OS 高频题](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
- [OS 进阶题](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)
