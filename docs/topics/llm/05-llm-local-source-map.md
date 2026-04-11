# LLM 本地参考源地图

## 1 分钟速答

你现在本地已经接入了几组很有价值的 LLM 开源参考源。它们不直接等于本仓库正文，但可以作为源码、目录结构、实践项目和专题讲解的参考层。

## 核心机制

### 已接入的本地参考仓库

- `external/llm-sources/llm_interview_note`
- `external/llm-sources/tiny-llm-zh`
- `external/llm-sources/tiny-rag`
- `external/llm-sources/tiny-mcp`
- `external/llm-sources/llama3-from-scratch-zh`

### 它们各自适合什么

| 仓库 | 作用 |
| --- | --- |
| `llm_interview_note` | 章节目录、面试知识体系、题目分层 |
| `tiny-llm-zh` | 小模型训练、tokenizer、推理参数、数据处理 |
| `tiny-rag` | RAG 链路、多路召回、重排 |
| `tiny-mcp` | MCP 基础、协议、server/client 实践 |
| `llama3-from-scratch-zh` | 从零实现 Llama3 的源码与讲解 |

### 推荐阅读顺序

1. 先用本仓库的 LLM 专题和题单建立主线
2. 再去 `llm_interview_note` 对照章节查漏
3. 需要动手时看 `tiny-llm-zh / tiny-rag / tiny-mcp`
4. 需要理解模型实现细节时看 `llama3-from-scratch-zh`

## 高频问法

- 为什么要同时保留“手册层”和“源码层”？
- 哪个仓库更适合补训练？哪个更适合补 RAG？
- 哪个仓库更适合理解模型实现？

## 深挖与误区

- 不要把外部仓库直接等同于你的面试答案
- 不要只 clone 不整理，最后还是找不到重点
- 不要把工程项目细节和面试主线混成一个层次
