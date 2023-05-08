# -*- coding: utf-8 -*-

pip install llama-index

import logging
import sys

### DEBUGモードにすればtoken数を確認できるぞ
#### logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

import os
os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"


# コンテンツ読み込み
from llama_index import download_loader
YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")
loader = YoutubeTranscriptReader()
documents = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=Pp6blsrQskY'],languages=['ja'])

# ベクトル化
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.indices.service_context import ServiceContext
service_context = ServiceContext.from_defaults(chunk_size_limit=3000)
index = GPTVectorStoreIndex.from_documents(documents,service_context=service_context)


# save to disk
#### index.storage_context.persist(persist_dir="./data/ytube230508.json")

# load from disk
#### from llama_index import StorageContext, load_index_from_storage
#### storage_context = StorageContext.from_defaults(persist_dir="./data/ytube230508.json")
#### index = load_index_from_storage(storage_context)


# query_engineをセット
query_engine = index.as_query_engine()

# クエリ実行
print(query_engine.query("何があったの？200文字以内で要約して"))

print(query_engine.query("概要を日本語で教えて？"))

print(query_engine.query("失敗の原因と考えられるものは？"))

print(query_engine.query("今後の予定は？"))