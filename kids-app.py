import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="Adira AI Fun Zone 🎈",
    page_icon="🧸",
    layout="centered"
)

# Custom CSS for colorful UI
st.markdown("""
    <style>
    body {
        background-color: #E3F2FD;
    }
    .stApp {
        background: linear-gradient(to bottom, #E3F2FD, #BBDEFB);
    }
    .title {
        font-size: 40px;
        color: #1565C0;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 20px;
        color: #0D47A1;
        text-align: center;
    }
    .answer-box {
        background-color: #FFF9C4;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎉 Adira AI Fun Zone 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything & get fun answers! 🧠✨</div>', unsafe_allow_html=True)

# Fun GIFs (safe cartoon vibes)
col1, col2 = st.columns(2)

with col1:
    st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", caption="Hi from Bluey! 🐶")

with col2:
    st.image("https://media.giphy.com/media/26gsspfbt1HfVQ9va/giphy.gif", caption="Peppa says Hello! 🐷")

st.write("---")

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Input
user_input = st.text_input("💡 Ask your question:")

# Button
if st.button("✨ Get Fun Answer ✨"):
    if user_input:
        with st.spinner("Thinking... 🤔💭"):
            response = llm.invoke(user_input)

            st.markdown(
                f'<div class="answer-box">🌈 {response.content}</div>',
                unsafe_allow_html=True
            )

            st.balloons()  # fun animation 🎈

    else:
        st.warning("🚨 Please ask something fun!")