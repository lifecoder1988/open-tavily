# open-tavily

## 运行步骤

- python3 -m venv .venv 创建虚拟环境
- source .venv/bin/activate 激活环境
- pip install -r requirement.txt 安装依赖
- 创建环境变量 .env 文件 参考 env.sample
- .venv/bin/uvicorn main:app 运行项目 开发环境使用 --reload 参数


## 支持的大模型 

- [x] 百川 


## 支持的向量数据库

- [x] milvus


## 重要项目依赖

- langchain_text_splitters 后面要去掉对langchain的依赖
- searxng 
- fastapi
- bs4 

## 路线

- [ ] 支持 openai embeding
- [ ] 并发抓取网页
- [ ] 支持第三方spider(low)
- [ ] 优化api时效性 5秒以内
- [ ] 增加日志
- [ ] 网络请求增加重试
- [ ] 支持docker部署
- [ ] 支持各种大语言模型
- [ ] 支持各种向量数据库
- [ ] 完善网页vector的更新机制(low)

## 检索优化思路

目标是控制在8秒以内

- 第一步是请求searxng 大概300毫秒
- 第二步是并发抓取网页，如果抓取过了就不要再抓取了 控制在4秒以内
- 第三步是调用接口计算embeding 控制在1秒内
  - 百川支持批量，但一批最多只有16个字符串
  - openai接口支持批量，一批最多2048个字符串
- 写入索引+检索 控制在1秒内
- 其他内存操作 1秒内
