from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import QianfanChatEndpoint

def chat_response(prompt,memory,api_key,secret_key):
    qianfan_chat = QianfanChatEndpoint(
        model="ERNIE-3.5-8K",
        temperature=0.2,
        api_key=api_key,
        secret_key=secret_key,
    )
    chain = ConversationChain(llm=qianfan_chat,memory=memory)
    response = chain.invoke({"input":prompt})
    return response["response"]
# memory = ConversationBufferMemory(return_messages=True)
# print(chat_response("物理学目前最前沿的理论是是什么？",memory,"KqqbeEq6uyKNM0FgnVapwCGM","S40RS2tFfbfmmRh9M19BoVLhmoAySbWo"))
# print(chat_response("我的上个问题是什么？",memory,"KqqbeEq6uyKNM0FgnVapwCGM","S40RS2tFfbfmmRh9M19BoVLhmoAySbWo"))
