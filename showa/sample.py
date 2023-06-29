import os
import sys
from dotenv import load_dotenv

load_dotenv()

# import logging
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# 読み込み
documents = SimpleDirectoryReader('spilitsVentures').load_data()
# documents = SimpleDirectoryReader('/data').load_data()

# index作成
index = VectorStoreIndex.from_documents(documents)

# 検索
query_engine = index.as_query_engine()
user_input = input("何を聞きたいですか？: ")
with_japanese = "日本語で回答してください。"
# 検索結果
response = query_engine.query(user_input + with_japanese)


print(response)