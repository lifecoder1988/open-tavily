from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm.baichuan import batch_embedding, embedding
from db import batch_insert, do_search


def get_chunks(content):
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.create_documents([content])

    result = []
    for item in chunks:
        result.append(item.page_content)
    # chunks = text_splitter.split_text(state_of_the_union)
    # print(chunks[0])
    # print(chunks[1])
    return result


def do_index(url, content):

    try:
        chunks = get_chunks(content)
        print(chunks)
        vectors = batch_embedding(chunks)

        data = []
        for i in range(0, len(chunks)):
            data.append({"vector": vectors[i], "url": url, "text": chunks[i]})
        batch_insert(data)
    except Exception as e:
        print(f"Error during query: {e}")


def search(query):
    vec = embedding(query)[0]
    results = do_search(vec)
    for result in results:
        print(result)
