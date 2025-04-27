import streamlit as st
import os  
import langchain 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import  MessagesPlaceholder,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.messages import HumanMessage

import warnings
warnings.filterwarnings("ignore")

parser=StrOutputParser()
groq_api_key=os.getenv("GROQ_API_KEY")
LLM=ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct",groq_api_key=groq_api_key)

# Chat history part 
from langchain_community.chat_message_histories import ChatMessageHistory 
from langchain_core.chat_history import BaseChatMessageHistory 
from langchain_core.runnables.history import RunnableWithMessageHistory 

if "store" not in st.session_state:
    st.session_state.store={}

def get_session_history(session_id:str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=ChatMessageHistory()
    return st.session_state.store[session_id]




generic_template="""
 You are recruiting agent for a company named Talent Scout .Your name is Repo and your primary job is to take information from the user.
 Ask the user about all the following details
 -Full Name
 -Email Address
 -Phone Number
 -Years of Experience
 -Desired Position(s)
 -Current Location
 -Tech Stack(including programming languages, frameworks, databases, and tools )
 When user starts the conversation ,greet the user introduce yourself to the user and tell about all the details you need
 require and explain him the whole procedure of this.
 Use {history} for checking whether you got all the information or not. If you did not get any information then 
 ask the user about that specific information and do this till you get all the information from the user.
 {input}
 
 Once you get all the details generate 5 moderate to high difficulty level Questions on the Tech Stack from the information provided. The questions 
 should have 4 options and ask the questions one by one .
 Once all the questions are answered , thank the user and say "We will get back to you shortly" in a more professional 
 manner and end the conversation.
 Have a professional tone and be professional in case the user says something irrelevant.
 Don't say about what are you gonna respond with . Just ask the questions 
  
 
 

"""

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',generic_template),
        ('user',"{input}"),
        MessagesPlaceholder(variable_name='history')
        
    ]
    
)


chain=prompt|LLM

with_message_history=RunnableWithMessageHistory(chain,get_session_history,input_messages_key='input', history_messages_key="history")

config={'configurable':{"session_id":"chat1"}}

st.title("Talent Scout | Smart Hiring Assistant 🤖")

st.write("Hello there candidate! Welcome to Talent Scout Recruitment Portal . Say 'Hi' for initiating the assistance!")




 
if "messages" not in st.session_state:
    st.session_state.messages = []

# for message in st.session_state.messages:
    # with st.chat_message(message["role"]):
        # st.markdown(message["content"])

user_input = st.chat_input("Type your message...")






if user_input:
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Thinking..."):
        response = with_message_history.invoke({"history":[HumanMessage(content=user_input)],'input':user_input},config)
        bot_reply = response.content
     
    if response and hasattr(response, "content") and response.content.strip():
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    else:
        st.session_state.messages.append({"role": "assistant", "content": "I'm sorry, I didn't catch that. Can you please repeat it ? "})


    
    # st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])




