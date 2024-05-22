# open-tavily

## 运行步骤

- python3 -m venv .venv 创建虚拟环境
- source .venv/bin/activate 激活环境
- pip install -r requirement.txt 安装依赖
- 创建环境变量 .env 文件 参考 env.sample
- .venv/bin/uvicorn main:app 运行项目 开发环境使用 --reload 参数
