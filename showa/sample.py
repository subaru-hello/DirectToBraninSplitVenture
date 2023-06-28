import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# os.environ["OPENAI_API_KEY"] = os.getenv('DATABASE_URL')

# import logging
import sys
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
args = sys.argv
first_arg = args[1] if len(args) > 1 else None
from llama_index import VectorStoreIndex, SimpleDirectoryReader
# 読み込み
documents = SimpleDirectoryReader('spilitsVentures').load_data()
# documents = SimpleDirectoryReader('/data').load_data()

# index作成
index = VectorStoreIndex.from_documents(documents)

# 検索
query_engine = index.as_query_engine()
user_input = input("何を聞きたいですか？: ")
# 検索結果
response = query_engine.query(user_input)


print(response)