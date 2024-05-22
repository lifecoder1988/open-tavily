import requests
from decouple import config


def search_searxng(query, token, instance_url="https://searxng.example.com"):
    """使用指定的 SearxNG 实例进行搜索。

    参数:
    - query: 搜索查询的字符串。
    - instance_url: SearxNG 实例的 URL。

    返回:
    - 搜索结果。
    """
    params = {
        "q": query,  # 搜索查询词
        "format": "json",  # 获取 JSON 格式的结果
        # "lang": "en",  # 搜索结果的语言
    }

    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(
            instance_url + "/search", headers=headers, params=params
        )
        response.raise_for_status()  # 检查请求是否成功
        return response.json()  # 返回 JSON 数据
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None


if __name__ == "__main__":
    searxng_token = config("SEARXNG_TOKEN")
    searxng_host = config("SEARXNG_HOST")
    print(searxng_token)
    result = search_searxng("周杰伦", searxng_token, searxng_host)
    print(result)
