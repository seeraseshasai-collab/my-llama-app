# App to build a simple chatbot
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Read .env file
load_dotenv()



# Get api key
gemini_key = os.getenv("GEMINI_API_KEY")

# Initialize the ollama client
gemini_client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=gemini_key)


print (gemini_key)

prompt = 'what is the best umbrella out there'

response = gemini_client.chat.completions.create(
    model = "gemini-2.5-flash-lite",
    messages = [{"role":"user","content": prompt} ]
)
print(response.choices[0].message.content)