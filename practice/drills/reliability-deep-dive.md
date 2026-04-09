# 可靠性与高并发深水区 Drill

适合：

- 主线已经走完一轮，开始准备中高级后端 / 基础架构 / 平台岗位
- 面试里已经能答基础题，但一追到一致性、故障恢复、I/O 模型就开始发虚
- 想把“看懂专题”变成“能稳定口述和举例”

## 怎么练

- 用 2 天到 4 天完成，不要拉太长
- 每次先用 5 分钟口述，再对照专题查漏
- 练完一定要录音或写 1 页复盘，不要只看

## Drill 1：分布式事务与补偿

先看：

- [分布式事务、补偿与一致性取舍](/Users/wizout/op/interview/docs/topics/backend/07-distributed-transactions-and-compensation.md)
- [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)

最小输出：

- 用 3 分钟解释 `2PC / TCC / SAGA / 本地消息表` 的区别
- 说清一个“为什么这里不用强一致事务”的业务场景
- 说清补偿、幂等、重试、对账分别负责什么

常见追问：

- 为什么很多电商链路更偏最终一致？
- 补偿失败怎么办？
- 对账为什么经常是最后的兜底？

## Drill 2：动态规划与状态设计

先看：

- [动态规划与状态设计](/Users/wizout/op/interview/docs/topics/algorithm/04-dp-and-state-design.md)
- [算法核心题清单](/Users/wizout/op/interview/questions/algorithm/00-must-know.md)

最小输出：

- 不写代码，直接口述 `爬楼梯`、`打家劫舍`、`最长递增子序列` 的状态和转移
- 解释为什么初始化往往比转移更容易错
- 解释什么时候优先用记忆化搜索，什么时候落成迭代 DP

常见追问：

- 怎么判断一个变量能不能成为状态？
- 空间优化什么时候成立？
- LIS 为什么还能做到 `O(n log n)`？

## Drill 3：epoll、慢请求与零拷贝

先看：

- [网络 I/O、epoll 与零拷贝](/Users/wizout/op/interview/docs/topics/operating-system/05-network-io-and-epoll.md)
- [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)

最小输出：

- 用 2 分钟解释 `select / poll / epoll` 的差别，不背表格
- 回答“为什么服务已经用了 epoll，还是会被慢请求拖垮”
- 解释零拷贝减少了哪些 copy，哪些成本还在

常见追问：

- epoll 解决的是就绪发现，还是业务处理？
- sendfile 和 mmap 各适合什么场景？
- 为什么线程池和下游依赖仍然会成为瓶颈？

## Drill 4：限流、降级与恢复

先看：

- [限流、降级与故障恢复](/Users/wizout/op/interview/docs/topics/system-design/06-rate-limiting-degradation-and-recovery.md)
- [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)

最小输出：

- 说清入口限流、用户维度限流、接口维度限流、下游限流分别拦什么
- 给一个真实业务，说明“先降什么、为什么”
- 解释为什么服务恢复阶段也会形成第二次事故

常见追问：

- 熔断和限流到底有什么区别？
- 恢复阶段为什么要预热和平滑放量？
- 缓存、MQ、数据库分别会在恢复阶段出现什么问题？

## 验收标准

- 每个 drill 都能先给 1 分钟结论，再展开到 3 分钟
- 能把概念题落到一个业务场景，而不是只背定义
- 面试官追问“为什么不用更强方案”时，你能讲出代价和取舍
- 录音回放后，能明确听出自己卡顿的具体点

## 建议复盘模板

- 我最容易把哪个题答成概念堆砌？
- 我有没有把“一致性目标 / 资源瓶颈 / 恢复策略”说完整？
- 我讲的是机制，还是能连到真实业务？
- 下一轮我需要补哪篇专题或哪组核心题？
