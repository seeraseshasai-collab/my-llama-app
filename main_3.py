# App to build a simple chatbot
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="My local AI Chatbot", page_icon=":robot_face:")
st.title("Llama 3.2 chatbot")
st.write("This is a simple app to build a chatbot using Llama 3.2. Ask a question and get the answer.")

# Initialize the ollama client
ollama_client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Initialize Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create input box
if prompt := st.chat_input("Enter a message"):
    # print raw data
    for m in st.session_state.messages:
        print(f"[{m['role'].upper()}]:{m['content']}")
    print("[ASSISTANT]:(waiting for generation...)")
    print("----------------------------------------\n")
    


    # Add question to notebook
    st.session_state.messages.append({"role":"user","content":prompt})

    #Show what user typed
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama_client.chat.completions.create(
                model="llama3.2",
                messages=st.session_state.messages
            )
        answer = response.choices[0].message.content
        st.markdown(answer)

        st.session_state.messages.append({"role":"assistant","content":answer})