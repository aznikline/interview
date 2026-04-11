# AI Infra 高频题

## 题目

occupancy 高是不是一定更快？

## 一句话回答

不是。occupancy 高只能说明 SM 上驻留的线程更多，真正性能还取决于访存、分支发散、寄存器压力和指令 mix。

## 展开回答

- occupancy 影响 latency hiding
- 但 memory bound / divergence 问题不会因为 occupancy 高就自动消失
- 高 occupancy 还可能伴随寄存器压力或 shared memory 约束

## 面试官追问

- occupancy 和吞吐是什么关系？
- 为什么有时低 occupancy 反而更快？

---

## 题目

为什么多卡训练往往会被通信拖慢？

## 一句话回答

因为计算可以分开做，但梯度、参数和激活同步需要消耗带宽和通信轮次，当模型规模和卡数上来后，通信很容易压过单卡计算收益。

## 展开回答

- AllReduce / AllGather / ReduceScatter 都有开销
- 网络拓扑和互联带宽直接影响同步成本
- 并行切分策略会改变通信模式

## 面试官追问

- 哪种并行更吃通信？
- NVLink 和 PCIe 差别为什么重要？
