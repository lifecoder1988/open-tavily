import requests
from decouple import config
from retrying import retry

@retry(stop_max_attempt_number=3, wait_fixed=500)
def embedding(input):
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


def chunk_list(lst, chunk_size):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


def batch_embedding(chunks):

    batched_chunks = chunk_list(chunks, 16)
    result = []
    for input in batched_chunks:
        result = result + embedding(input)

    return result
