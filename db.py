from pymilvus import connections, Collection, utility
from pymilvus import Collection, CollectionSchema, FieldSchema, DataType
from decouple import config
import time
from llm.llm import get_llm

conn = connections.connect("default", uri=config("DB_URI"), token=config("DB_TOKEN"))

backend_llm = get_llm()

# 定义字段
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(
        name="vector", dtype=DataType.FLOAT_VECTOR, dim=backend_llm.get_dim_size()
    ),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=5000),
    FieldSchema(name="url", dtype=DataType.VARCHAR, max_length=2048),
]

# 创建集合的 schema
schema = CollectionSchema(fields, description="Keyword search collection")

# 创建集合
collection_name = config("EMBEDDIN_COLLECTION_NAME")

collection = Collection(name=collection_name, schema=schema, using="default")

index_params = {
    "metric_type": "COSINE",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 100},
}
collection.create_index("vector", index_params)

collection.load()


def getConnection():
    return conn


def is_doc_exist(url):
    # 构建查询表达式
    query_expression = f"url == '{url}'"

    # 执行查询
    query_results = collection.query(expr=query_expression)

    # 检查结果
    if query_results:
        return True
    return False


def batch_insert(data):

    # print(data)
    insert_result = collection.insert(data)
    print("Number of inserted entities:", len(insert_result.primary_keys))


def do_search(vec):

    print("start db search")
    start_time = time.time()
    collection.load()
    end_time = time.time()
    print(f"Collection loaded in {end_time - start_time} seconds.")

    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
    results = collection.search(
        [vec], "vector", search_params, output_fields=["text", "url"], limit=10
    )
    # for result in results:
    #    print(result)
    return results


if __name__ == "__main__":
    check_collection = utility.has_collection("test")
    print(check_collection)
