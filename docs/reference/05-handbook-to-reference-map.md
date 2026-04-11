# 手册层与原始层映射

## 目的

这页解决一个具体问题：

- 手册层适合复习和答题
- 原始层适合看完整目录、源码和项目实践

你需要知道“我现在在手册里看到的这一块，对应到原始层应该去哪看”。

## LLM

| 手册层 | 原始层优先参考 |
| --- | --- |
| [LLM 基础与术语](../topics/llm/01-llm-foundations.md) | [llm_interview_note/01.大语言模型基础](../../references/llm_interview_note/01.大语言模型基础) |
| [LLM 架构与训练](../topics/llm/02-llm-architecture-and-training.md) | [llm_interview_note/02.大语言模型架构](../../references/llm_interview_note/02.大语言模型架构) / [04.分布式训练](../../references/llm_interview_note/04.分布式训练) |
| [LLM 推理与 Serving](../topics/llm/03-llm-inference-and-serving.md) | [llm_interview_note/06.推理](../../references/llm_interview_note/06.推理) / [tiny-llm-zh](../../references/tiny-llm-zh) |
| [RAG、Agent、MCP 与评估](../topics/llm/04-rag-agent-eval.md) | [tiny-rag](../../references/tiny-rag) / [tiny-mcp](../../references/tiny-mcp) / [llm_interview_note/09.大语言模型评估](../../references/llm_interview_note/09.大语言模型评估) |
| [LLM 本地参考源地图](../topics/llm/05-llm-local-source-map.md) | [LLM 参考源索引](01-llm-source-index.md) |

## AI Infra

| 手册层 | 原始层优先参考 |
| --- | --- |
| [CUDA 与 GPU 基础](../topics/ai-infra/01-cuda-and-gpu-basics.md) | [ai-infra-hpc/01chip](../../references/ai-infra-hpc/01chip) / [02hpc/05cuda](../../references/ai-infra-hpc/02hpc/05cuda) |
| [通信、互联与训练并行](../topics/ai-infra/02-communication-and-parallelism.md) | [ai-infra-hpc/03link](../../references/ai-infra-hpc/03link) / [05ccl](../../references/ai-infra-hpc/05ccl) |
| [训练系统与 Serving](../topics/ai-infra/03-training-and-serving-systems.md) | [ai-infra-hpc/06trainAndInfer](../../references/ai-infra-hpc/06trainAndInfer) / [OriginDL/docs/design](../../references/OriginDL/docs/design) |
| [AI Infra 本地参考源地图](../topics/ai-infra/04-local-source-map.md) | [AI Infra 参考源索引](02-ai-infra-source-index.md) |

## AI 编译器

| 手册层 | 原始层优先参考 |
| --- | --- |
| [AI 编译器专题](../topics/ai-compiler/00-index.md) | [llama3-from-scratch-zh](../../references/llama3-from-scratch-zh) 作为模型实现补充，结合官方 MLIR / XLA / Triton 文档 |

## 使用建议

- 先用手册层建立主线
- 再用原始层补完整目录和源码细节
- 不要直接把原始层当面试答案背诵
