#!/usr/bin/python3
# -*- coding: utf-8 -*-            
# @Author :le
# @Time : 2025/3/11 18:05

from config import settings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter


class DataProcess:

    @staticmethod
    def process():
        """
        数据加载与分割
        :return:
        """
        loader = TextLoader(settings.DOCUMENTS_PATH)
        documents = loader.load()

        text_splitter = CharacterTextSplitter(
            separator=r'\d+\.',
            chunk_size=150,
            chunk_overlap=0,
            length_function=len,
            is_separator_regex=True,
        )
        docs = text_splitter.split_documents(documents)
        return docs


