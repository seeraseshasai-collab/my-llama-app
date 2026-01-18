# App to build a simple chatbot
import streamlit as st
from openai import OpenAI


st.set_page_config(page_title="My local AI Chatbot", page_icon=":robot_face:")
st.title("Gemini cloud chatbot")
st.write("This is a simple app to build a chatbot using gemini 2.5 flash lite. Ask a question and get the answer.")

# Get API key from streamlit secrets
if "GEMINI_API_KEY" in st.secrets:
    gemini_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("API key not found! please add it to secrets")
    st.stop()

# Initialize the ollama client
gemini_client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=gemini_key)

# Initialize Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Add a sidebar to clear chat

if st.sidebar.button("Clear Chat Hisotry"):
    st.session_state.messages = []
    st.rerun()


# Create input box
if prompt := st.chat_input("Enter a message"):
    st.session_state.messages.append({"role":"user","content":prompt})
    #Show what user typed
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response with streaming
    with st.chat_message("assistant"):
        
        stream = gemini_client.chat.completions.create(
            model="gemini-2.5-flash-lite",
            messages=st.session_state.messages,
            stream=True,
            )
        full_response = st.write_stream(stream)
        
        #st.markdown(response.choices[0].message.content)
    # Add response to history    
    st.session_state.messages.append({"role":"assistant","content":full_response})    