# AI Infra 路线

适合：

- 目标岗位是推理引擎、AI Infra、模型服务、编译优化、系统加速
- 想把后端 / OS / 系统设计和 AI 编译器专题串成一条面试主线
- 面试中会同时被问到服务稳定性、runtime 和性能指标

## 目标岗位

- 推理引擎工程师
- AI 编译器工程师
- 模型加速 / 系统优化工程师
- LLM Serving / Runtime 工程师

## 核心准备顺序

1. 后端基础与并发模型
2. 操作系统与性能分析
3. 系统设计与容量推理
4. AI 编译器专题
5. LLM 推理性能优化案例

## 4 周起手计划

### Week 1：先保底座

- 看 [后端核心题清单](/Users/wizout/op/interview/questions/backend/00-must-know.md)
- 看 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
- 看 [OS 场景地图](/Users/wizout/op/interview/docs/topics/operating-system/06-os-scenario-map.md)
- 跑 [OS 14 天计划](/Users/wizout/op/interview/tracks/os-14d/README.md)
- 跑 [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)

最低输出：

- 能讲并发、I/O、线程模型和高并发服务之间的关系
- 能把 `epoll / 零拷贝 / 内存屏障` 讲到性能现象上

### Week 2：AI 编译器主链路

- 看 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
- 看 [AI 编译器进阶题](/Users/wizout/op/interview/questions/ai-compiler/deep-dive.md)
- 看 [IR、Lowering 与 Dialect](/Users/wizout/op/interview/docs/topics/ai-compiler/02-ir-lowering-and-dialects.md)

最低输出：

- 能把 `模型/图 -> IR -> lowering -> fusion -> kernel -> runtime -> 指标` 串成一条链路
- 能讲清 compile time 和 runtime 的边界

### Week 3：Serving 与系统设计

- 看 [系统设计核心题清单](/Users/wizout/op/interview/questions/system-design/00-must-know.md)
- 看 [Serving Runtime 与在线调度](/Users/wizout/op/interview/docs/topics/ai-compiler/05-serving-and-runtime-systems.md)
- 看 [AI 编译器项目表达稿](/Users/wizout/op/interview/projects/ai-compiler-case-studies/project-storytelling.md)

最低输出：

- 能解释 `TTFT / TPOT / throughput / P99` 的 trade-off
- 能把 batching、KV cache、admission control、恢复策略连到服务侧

### Week 4：Mock 与指标承压

- 做 [AI Infra Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-infra.md)
- 做 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)
- 跑 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

最低输出：

- 能在连续追问下保持 `层次边界 / 指标 / 瓶颈 / 边界`
- 能讲一个可信的优化故事，而不是框架名堆砌

## 额外加分项

- GPU 基础：warp、shared memory、occupancy
- 模型推理：batching、prefill、decode、KV cache
- 编译器基础：IR、SSA、pass pipeline

## 只剩 7 天怎么压缩

1. 先过 [AI 编译器核心题清单](/Users/wizout/op/interview/questions/ai-compiler/00-must-know.md)
2. 再过 [操作系统核心题清单](/Users/wizout/op/interview/questions/operating-system/00-must-know.md)
3. 跑 [OS 与 AI 编译器口述速答包](/Users/wizout/op/interview/practice/drills/os-and-ai-compiler-oral-pack.md)
4. 做 [AI 编译器深挖 Mock](/Users/wizout/op/interview/practice/mock-interviews/ai-compiler-deep-dive.md)
5. 最后跑 [追问压测包](/Users/wizout/op/interview/practice/drills/follow-up-pressure-pack.md)

## 最容易失分的地方

- 只会背 MLIR、TVM、XLA、Triton 名字
- 不会讲 compile time / runtime 的边界
- 只讲平均耗时，不讲 TTFT、TPOT、P99 和显存
- 不会把优化落到 workload 和业务目标
