# AI Infra 本地参考源地图

## 1 分钟速答

你现在本地已经有两组很有价值的 AI Infra 参考仓库：`ai-infra-hpc` 和 `OriginDL`。它们不直接等于你的面试答案，但特别适合补 `CUDA / 多卡通信 / 训练并行 / 框架底层实现` 这部分的理解。

## 核心机制

### 已接入的本地参考仓库

- `external/ai-infra-sources/ai-infra-hpc`
- `external/ai-infra-sources/OriginDL`

### 它们各自适合什么

| 仓库 | 作用 |
| --- | --- |
| `ai-infra-hpc` | CUDA、通信、并行、AI Infra/HPC 方向的知识与实践参考 |
| `OriginDL` | 从零实现类 PyTorch 深度学习框架、自动微分、CUDA matmul、训练/推理链路参考 |

### 推荐使用方式

1. 先用本仓库的 AI Infra 专题和题单建立主线
2. 再用 `ai-infra-hpc` 补 CUDA / HPC / 通信细节
3. 再用 `OriginDL` 看框架底层和训练推理实现

## 高频问法

- 为什么要同时保留“手册层”和“源码层”？
- 哪个仓库更适合补 CUDA？哪个更适合理解框架底层？
- 哪个仓库更适合讲项目实践？

## 深挖与误区

- 不要 clone 了就等于学会了
- 不要把源码实现细节直接当面试答案
- 不要只看 README，不看目录结构和模块边界
