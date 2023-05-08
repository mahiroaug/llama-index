# -*- coding: utf-8 -*-

pip install llama-index

import logging
import sys

### DEBUGモードにすればtoken数を確認できるぞ
#### logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

import os
os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"


# コンテンツ読み込み
from llama_index.readers import BeautifulSoupWebReader
documents = BeautifulSoupWebReader().load_data(urls=["https://docs.fireblocks.com/api/v1/swagger.yaml"])

# ベクトル化
from llama_index import GPTVectorStoreIndex
index = GPTVectorStoreIndex.from_documents(documents=documents)


# save to disk
#### index.storage_context.persist(persist_dir="./data/fireblocks.json")

# load from disk
#### from llama_index import StorageContext, load_index_from_storage
#### storage_context = StorageContext.from_defaults(persist_dir="./data/fireblocks.json")
#### index = load_index_from_storage(storage_context)


# query_engineをセット
query_engine = index.as_query_engine()

# クエリ実行
print(query_engine.query("Get the asset balance for a vault account"))

print(query_engine.query("valut accountの口座残高を取得するには？日本語で答えて"))

print(query_engine.query("valut accountの口座残高を取得し、表示するpythonコードを書いて"))

print(query_engine.query("valut accountのアドレスと口座残高を取得し、表示するpythonコードを書いて"))