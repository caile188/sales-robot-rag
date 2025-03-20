#!/usr/bin/python3
# -*- coding: utf-8 -*-            
# @Author :le
# @Time : 2025/3/12 10:19
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from config import settings
from langchain_core.runnables import RunnableLambda
import re


class RetrievalChain:

    @staticmethod
    def get_chain(retriever):
        llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            temperature=0,
            max_tokens=600
        )

        system_prompt = """你是一名严格遵循规范的装修顾问，必须按照以下规则回答：
                        1. **仅使用**提供的上下文信息生成答案，禁止任何形式的联网搜索或外部知识调用
                        2. 若上下文无答案，回复指定话术：您的问题需要专业人员解答，稍后会有顾问联系您
                        
                        上下文：{context}
                        """

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}")
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, prompt)

        chain = create_retrieval_chain(retriever, question_answer_chain) | RunnableLambda(RetrievalChain.final_validate)
        # chain = create_retrieval_chain(retriever, question_answer_chain)
        return chain

    @staticmethod
    def final_validate(output):
        """
        最终校验，输出 后处理，保证输出信息规范化
        """
        context = output["context"]
        answer = output["answer"]
        # 检测违规内容
        if not context or re.search(r'http[s]?://', answer):
            return "您的问题需要专业人员解答，稍后会有顾问联系您"
        return answer
