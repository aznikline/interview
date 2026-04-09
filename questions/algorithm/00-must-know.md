# 算法核心题清单

## 题目

算法面试最值得优先刷哪些模式，顺序应该怎么排？

## 一句话回答

优先刷覆盖面最大的模式：`滑动窗口 -> 双指针 -> 二分 -> 树/图搜索 -> 回溯 -> 堆与并查集 -> DP`。顺序上先练模式识别，再练口述，再练边界和变体。

## 展开回答

### 第一层：必须拿下的高频模式

这部分是算法面试的主干：

- 滑动窗口：最长无重复子串、最小覆盖子串
- 双指针：两数之和、三数之和、盛最多水的容器
- 二分：查找、边界查找、二分答案
- 二叉树：层序遍历、最近公共祖先、路径和
- 图搜索：岛屿数量、课程表、最短路径基础
- 回溯：全排列、子集、组合总和
- 堆：top k、合并 k 个有序链表
- 并查集：连通性、冗余连接
- DP：爬楼梯、打家劫舍、最长递增子序列、背包

### 第二层：每类模式都要会说什么

每做一题，都要先回答这几个问题：

- 这题属于什么模式
- 为什么这个模式适合
- 核心不变量或状态是什么
- 时间复杂度和空间复杂度是什么
- 边界条件有哪些

### 第三层：建议刷题顺序

1. 先看 [算法专题首页](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
2. 再看 [算法方法论](/Users/wizout/op/interview/docs/topics/algorithm/01-algorithm-methodology.md)
3. 再看 [高频模式](/Users/wizout/op/interview/docs/topics/algorithm/02-common-patterns.md)
4. 再看 [框架、例题和训练法](/Users/wizout/op/interview/docs/topics/algorithm/03-frameworks-and-drills.md)
5. 然后刷 [算法高频题](/Users/wizout/op/interview/questions/algorithm/high-frequency.md)
6. 最后刷 [模式与 DP](/Users/wizout/op/interview/questions/algorithm/patterns-and-dp.md)

### 第四层：最小交付标准

每个模式至少要做到：

- 能举出 `2` 道代表题
- 能口述 `1` 份模板思路
- 能指出 `2` 个常见坑
- 能讲出 `1` 个面试官追问

## 面试官追问

- 为什么这题想到滑窗而不是哈希暴力？
- 为什么这题不是贪心？
- DFS 和 BFS 怎么选？
- DP 的状态为什么这么定义？
- 如何把这题从暴力优化到线性或对数复杂度？

## 易错点

- 代码会写，但思路讲不清
- DP 状态定义不清
- 忽略初始化和边界条件
- 看到变体题就脱离原有模式

## 关联知识点

- [算法专题首页](/Users/wizout/op/interview/docs/topics/algorithm/00-index.md)
- [算法高频题](/Users/wizout/op/interview/questions/algorithm/high-frequency.md)
- [算法进阶题](/Users/wizout/op/interview/questions/algorithm/patterns-and-dp.md)
- [算法框架与训练法](/Users/wizout/op/interview/docs/topics/algorithm/03-frameworks-and-drills.md)
