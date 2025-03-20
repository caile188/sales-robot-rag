#!/usr/bin/python3
# -*- coding: utf-8 -*-            
# @Author :le
# @Time : 2025/3/11 19:03

import os
import sys
from config import settings
from modules.data_process import DataProcess
from modules.vector_store import VectorStore
from modules.retrieval_chain import RetrievalChain
import gradio as gr


def main(message, history):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # 数据存储与加载
    vector_store_obj = VectorStore()
    if not os.path.exists(settings.DB_PATH):
        docs = DataProcess.process()
        db = vector_store_obj.create_db(docs)
    else:
        db = vector_store_obj.load_db()

    # 检索，
    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"score_threshold": 0.8}
    )
    chain = RetrievalChain.get_chain(retriever)
    result = chain.invoke({"input": message})

    return result


def launch_gradio():
    demo = gr.ChatInterface(
        fn=main,
        type="messages",
        title="家装顾问",
        chatbot=gr.Chatbot(height=550, type="messages")
    )

    demo.launch(server_name="0.0.0.0", share=False)


if __name__ == "__main__":
    launch_gradio()




