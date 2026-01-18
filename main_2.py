import streamlit as st
import time
from openai import OpenAI




ollama_client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# function to stream the data
def stream(text,delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)




if prompt := st.chat_input("Enter a prompt:"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama_client.chat.completions.create(
                model="llama3.2",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
        st.markdown(response.choices[0].message.content)
        #st.write_stream(stream(output))

