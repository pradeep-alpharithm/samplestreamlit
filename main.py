import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the GROQ_API_KEY from the environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'

def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant that answers questions."
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content

# Streamlit app title
st.title("Simple Search App")

# Input box for user query
query = st.text_input("Enter your query:")

# Button to get response
if st.button("Search"):
    if query:
        # Get the response from the Groq model
        response = get_groq_response(query)
        # Display the response
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")
