# OS 与 AI 编译器口述速答包

适合：

- 面试临近，需要把 OS 和 AI 编译器从“看过”变成“能稳定说”
- 这两块经常被问，但答题结构还不够稳
- 想在一轮练习里同时覆盖基础机制和性能优化表达

## 使用方法

- 一轮练习控制在 30 分钟到 45 分钟
- OS 每题先答 1 分钟，再补 1 分钟工程现象
- AI 编译器每题先答 1 分钟，再补 1 分钟指标和边界
- 练完后只记录最卡的 3 个点，不继续扩资料

## Round 1：OS 核心 10 题

按这个顺序口述：

1. 进程和线程区别是什么？
2. 线程切换为什么贵？
3. 用户态和内核态如何切换？
4. 虚拟内存解决了什么？
5. page fault 为什么会抖？
6. select / poll / epoll 最大差别是什么？
7. 为什么 epoll 服务也会被慢请求拖垮？
8. 零拷贝减少了什么成本？
9. false sharing 是什么？
10. 内存屏障为什么重要？

每题最低要补：

- 一个系统现象
- 一个性能代价
- 一个观测或缓解动作

## Round 2：AI 编译器核心 10 题

按这个顺序口述：

1. AI 编译器和传统编译器最大区别是什么？
2. 为什么要多级 IR？
3. lowering 在做什么？
4. 算子融合为什么能提速？
5. 融合为什么有时会变慢？
6. layout 为什么影响性能？
7. 动态 shape 为什么难？
8. 编译器和 runtime 怎么分工？
9. decode 为什么常 memory bound？
10. 怎么证明一个优化真的有效？

每题最低要补：

- 它位于哪一层
- 它解决了什么瓶颈
- 它影响哪个指标
- 一个边界或反例

## Round 3：跨域追问压测

如果前两轮已经稳定，再补这组追问：

- 为什么 epoll 不是高并发银弹？
- 为什么零拷贝不是完全零成本？
- 为什么 runtime 不能完全替代编译优化？
- 为什么动态 shape 会把 runtime 拉进来？
- 为什么 decode 阶段优化常常受内存带宽限制？
- 如果面试官继续追问到底层实现，你先展开哪一层？

## 合格标准

- 1 分钟回答能先给结论，不散
- 展开时能同时补机制和性能结果
- 不会把 OS 讲成纯教材，也不会把 AI 编译器讲成框架名背诵
- 被追问时能自然转到指标、瓶颈和边界

## 推荐搭配

- 看 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- 看 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- 做 [AI Infra Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-infra.md)
- 做 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)
