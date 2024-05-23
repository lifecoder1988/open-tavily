import requests
from openai import OpenAI
from decouple import config
from retrying import retry
from llm.base_llm import BaseLLM

modelConfig = {
    "text-embedding-3-large": {"dim": 3072, "token": 2048},
    "text-embedding-3-small": {"dim": 1536, "token": 2048},
    "text-embedding-ada-002": {"dim": 1536, "token": 2048},
}


class OpenaiLLM(BaseLLM):
    def __init__(self, url, api_key, model):
        # 调用父类构造器
        self.client = OpenAI(api_key=api_key, base_url=url)

        super().__init__(url, api_key, model)

    def get_token_limit(self):
        return modelConfig[self.get_model()]["token"]

    def get_chunk_limit(self):
        return 1000

    def get_batch_size(self):
        return 200

    def get_dim_size(self):
        return modelConfig[self.get_model()]["dim"]

    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    def embedding(self, inputs):
        # 配置 API URL 和你的 OpenAI API 密钥
        print(
            f"openai start create embeding count: {len(inputs)} size {len(inputs[0])}"
        )

        print(self.client.base_url)
        data = self.client.embeddings.create(input=inputs, model=self.get_model())
        result = []

        if not hasattr(data, "data"):
            print("Failed to fetch embeddings:", data)
            return []

        for item in data.data:
            result.append(item.embedding)

        print("Query for embeddings successful.")
        return result
