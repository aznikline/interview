# 操作系统核心题清单

## 题目

后端面试里的操作系统最该准备哪些题？

## 一句话回答

优先准备能解释性能和并发现象的题：进程线程、上下文切换、虚拟内存、epoll、多路复用、锁、false sharing、内存屏障。

## 展开回答

### 第一优先级：必须会讲

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

### 准备目标

- 不能只背概念
- 必须能映射到后端问题
- 必须知道它和性能 / 并发 / I/O 的关系

## 面试官追问

- 为什么 epoll 服务还会被慢请求拖垮？
- 协程为什么不是万能方案？
- 锁竞争和 false sharing 有什么区别？

## 易错点

- 只会教材定义
- 不会结合真实服务
- 不会讲系统层开销

## 关联知识点

- [操作系统专题首页](/Users/wizout/op/interview/docs/topics/operating-system/00-index.md)
- [OS 高频题](/Users/wizout/op/interview/questions/operating-system/high-frequency.md)
- [OS 进阶题](/Users/wizout/op/interview/questions/operating-system/concurrency-and-memory.md)

