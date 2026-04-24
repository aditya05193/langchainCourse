import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.6
)

# UI Title
st.title("💬 AI  for Adira Family ....")

# Input box
user_input = st.text_input("Ask your question:")

# Button
if st.button("Get Answer"):
    if user_input:
        with st.spinner("Thinking... 🤔"):
            response = llm.invoke(user_input)
            st.success(response.content)
    else:
        st.warning("Please enter a question")