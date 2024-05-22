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
