from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')


st.title('CHATBOT')
st.markdown("MY QNA BOT ")

#  session storage session state streamlit bacup memory
if 'messages' not in st.session_state:
    st.session_state.messages=[]


for messages in st.session_state.messages:
    role=messages['role']
    content=messages['content']
    st.chat_message(role).markdown(content)

query=st.chat_input('ASK ANYTHING -')

if query:
    st.session_state.messages.append({'role':'user','content':'query'})
    st.chat_message('user').markdown(query)
    res=llm.invoke(query)
    st.chat_message('ai').markdown(res.content)
    st.session_state.messages.append({'role':"ai",'content':res.content})

# while True:
#     query=input()

#     if query.lower() in ['quit','exit','bye']:
#         print('good bye')
#         break()
    
#     res=llm.invoke(query)

#     print("AI ", res.content,'\n')
