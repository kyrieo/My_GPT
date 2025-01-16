import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import chat_response
st.title("	:robot_face: 我的聊天机器人")
with st.sidebar:
    ak = st.text_input("请输入千帆模型的api_key",type="password")
    sk = st.text_input("请输入千帆模型的secret_key",type="password")
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["message"] = [{
        "role":"ai",
        "content":"你好，我是Ren_GPT,有什么可以帮你的吗？"
    }]
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])
prompt = st.chat_input()
if prompt and not ak:
    st.info("请输入千帆模型的spi_key")
    st.stop()
if prompt and not sk:
    st.info("请输入千帆模型的secret_key")
    st.stop()
if prompt:
    st.session_state["message"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)
    with st.spinner(("AI正在思考，请稍等...")):
        response = chat_response(prompt,st.session_state["memory"],ak,sk)
    st.session_state["message"].append({"role":"ai","content":response})
    st.chat_message("ai").write(response)
# if button :
#
#     st.write(response)