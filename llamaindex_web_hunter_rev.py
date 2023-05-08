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
documents = BeautifulSoupWebReader().load_data(urls=["https://mangapedia.com/HUNTER%C3%97HUNTER-zp9bl6i8k"])

# ベクトル化
from llama_index import GPTVectorStoreIndex
index = GPTVectorStoreIndex.from_documents(documents=documents)


# save to disk
#### index.storage_context.persist(persist_dir="./data/hunter230508.json")

# load from disk
#### from llama_index import StorageContext, load_index_from_storage
#### storage_context = StorageContext.from_defaults(persist_dir="./data/hunter230508.json")
#### index = load_index_from_storage(storage_context)


# query_engineをセット
query_engine = index.as_query_engine()

# クエリ実行
print(query_engine.query("クラピカの能力は？"))

print(query_engine.query("ゾルディック家について説明せよ"))

print(query_engine.query("ゴンの母親は誰？どういう人物？"))

print(query_engine.query("キメラアント編を要約して"))

print(query_engine.query("あらすじを200字以内で説明して"))