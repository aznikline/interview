# Operating Systems Week Plan

适用场景：

- 你要在 `5-7` 天内快速把 OS 和并发问题讲顺
- 你希望把 OS 从“课本”转成“后端性能解释器”

## Day 1：进程、线程、调度

- 阅读 [01-os-core.md](../../docs/topics/operating-system/01-os-core.md)
- 聚焦：
  - 进程 vs 线程
  - 上下文切换
  - 用户态 / 内核态
- 输出：解释为什么线程切换贵

## Day 2：虚拟内存

- 阅读 [02-memory-and-io.md](../../docs/topics/operating-system/02-memory-and-io.md)
- 聚焦：
  - 虚拟内存
  - 页表
  - TLB
  - page fault
- 输出：讲清为什么 page fault 会放大尾延迟

## Day 3：I/O 与多路复用

- 阅读 [02-memory-and-io.md](../../docs/topics/operating-system/02-memory-and-io.md)
- 聚焦：
  - 阻塞 / 非阻塞
  - select / poll / epoll
  - 慢请求拖垮服务
- 输出：解释 epoll 为什么不是万能药

## Day 4：零拷贝与大流量

- 回看 [OS 核心题清单](../../questions/operating-system/00-must-know.md)
- 聚焦：
  - zero-copy
  - sendfile
  - mmap
- 输出：讲清减少了什么拷贝，没减少什么成本

## Day 5：锁、内存模型、false sharing

- 阅读 [03-concurrency-and-scheduling.md](../../docs/topics/operating-system/03-concurrency-and-scheduling.md)
- 聚焦：
  - 锁竞争
  - 内存屏障
  - false sharing
- 输出：比较锁竞争和 false sharing 的区别

## Day 6：和后端问题联动

- 回看 [后端核心题清单](../../questions/backend/00-must-know.md)
- 把 OS 问题挂到：
  - 网络服务
  - 高并发请求
  - 热点更新
  - 慢查询或慢 I/O
- 输出：至少完成 `3` 个“系统机制 -> 工程现象”例子

## Day 7：口述与复盘

- 刷 [OS 高频题](../../questions/operating-system/high-frequency.md)
- 刷 [并发与内存题](../../questions/operating-system/concurrency-and-memory.md)
- 输出：
  - `8-10` 个 OS 高频题答案
  - 一份最薄弱 OS 概念清单
