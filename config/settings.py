#!/usr/bin/python3
# -*- coding: utf-8 -*-            
# @Author :le
# @Time : 2025/3/11 16:53
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCUMENTS_PATH = os.path.join(BASE_DIR, 'data/documents/home_decoration_sales_data.txt')
DB_PATH = os.path.join(BASE_DIR, 'data/db')
OPENAI_MODEL = 'gpt-4o'
EMBEDDING_MODEL = 'text-embedding-ada-002'
