# open-tavily

## 运行步骤

- python3 -m venv .venv 创建虚拟环境
- source .venv/bin/activate 激活环境
- pip install -r requirement.txt 安装依赖
- 创建环境变量 .env 文件 参考 env.sample
- .venv/bin/uvicorn main:app 运行项目 开发环境使用 --reload 参数

## windows

- .venv\Scripts\activate 激活环境

## 支持的大模型

- [x] 百川
- [x] openai

## 支持的向量数据库

- [x] milvus

## 重要项目依赖

- langchain_text_splitters 后面要去掉对 langchain 的依赖
- searxng
- fastapi
- bs4

## 路线

- [x] 支持 openai embeding
- [x] 并发抓取网页
- [ ] 支持第三方 spider(low)
- [ ] 优化 api 时效性 5 秒以内
- [ ] 增加日志
- [x] 网络请求增加重试
- [ ] 支持 docker 部署
- [ ] 支持各种大语言模型
- [ ] 支持各种向量数据库
- [ ] 完善网页 vector 的更新机制(low)
- [ ] config 统一管理
- [ ] 数据库连接重试

## 检索优化思路

目标是控制在 8 秒以内

- 第一步是请求 searxng 大概 300 毫秒
- 第二步是并发抓取网页，如果抓取过了就不要再抓取了 控制在 4 秒以内
- 第三步是调用接口计算 embeding 控制在 1 秒内
  - 百川支持批量，但一批最多只有 16 个字符串
  - openai 接口支持批量，一批最多 2048 个字符串
- 写入索引+检索 控制在 1 秒内
- 其他内存操作 1 秒内
