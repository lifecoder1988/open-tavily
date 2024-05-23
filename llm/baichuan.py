import requests
from decouple import config
from retrying import retry
from llm.base_llm import BaseLLM


class BaichuanLLM(BaseLLM):
    def __init__(self, url, api_key, model):
        # 调用父类构造器
        super().__init__(url, api_key, model)

    def get_token_limit(self):
        return 500

    def get_batch_size(self):
        return 16

    def get_chunk_limit(self):
        return 500

    def get_dim_size(self):
        return 1024

    @retry(stop_max_attempt_number=3, wait_fixed=500)
    def embedding(self, input):
        # 配置 API URL 和你的 Baichuan API 密钥
        url = "http://api.baichuan-ai.com/v1/embeddings"
        baichuan_api_key = config("BAICHUAN_API_KEY")

        # 设置请求头部
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {baichuan_api_key}",
        }

        # 构造请求体数据
        data = {"model": "Baichuan-Text-Embedding", "input": input}

        print("start query embedding...")
        # 发送 POST 请求
        response = requests.post(url, json=data, headers=headers)
        data = response.json()
        result = []

        if "data" not in data:
            print(data)

        for item in data["data"]:
            result.append(item["embedding"])

        print("query embedding success")
        return result
