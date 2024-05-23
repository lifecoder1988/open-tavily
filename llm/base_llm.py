def chunk_list(lst, chunk_size):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


class BaseLLM:
    def __init__(self, url, api_key, model):
        self.url = url
        self.api_key = api_key
        self.model = model

    def get_model(self):
        return self.model

    def get_chunk_limit(self):
        pass

    def embedding(self, input):
        pass

    def batch_embedding(self, chunks):

        batched_chunks = chunk_list(chunks, self.get_batch_size())
        result = []
        for input in batched_chunks:
            result = result + self.embedding(input)

        return result

    def get_token_limit(self):
        pass

    def get_batch_size(self):
        pass

    def get_dim_size(self):
        pass
