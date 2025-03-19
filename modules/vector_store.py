#!/usr/bin/python3
# -*- coding: utf-8 -*-            
# @Author :le
# @Time : 2025/3/11 18:45

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import settings


class VectorStore:
    """
    向量存储
    """
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
        self.db_path = settings.DB_PATH

    def create_db(self, docs):
        db = FAISS.from_documents(docs, self.embeddings)
        db.save_local(self.db_path)
        return db

    def load_db(self):
        return FAISS.load_local(
            self.db_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )
