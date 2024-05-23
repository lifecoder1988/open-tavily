from decouple import config
from llm.baichuan import BaichuanLLM
from llm.openai import OpenaiLLM


def get_llm():
    embedding_provider = config("EMBEDDING_PROVIDER")

    if embedding_provider == "baichuan":
        return BaichuanLLM(
            config("BAICHUAN_URL"),
            config("BAICHUAN_API_KEY"),
            config("BAICHUAN_EMBEDDING_MODAL"),
        )
    elif embedding_provider == "openai":
        return OpenaiLLM(
            config("OPENAI_URL"),
            config("OPENAI_API_KEY"),
            config("OPENAI_EMBEDDING_MODAL"),
        )
    else:
        raise ValueError("embedding_provider unsupported")
