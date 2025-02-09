import openai
import streamlit as st

# Your OpenAI API key
openai.api_key = "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"


# Function to call OpenAI's GPT-3.5-Turbo for a chat response
def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest available model (gpt-3.5-turbo)
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app UI setup
st.title("ChatGPT Clone")
st.markdown("""
This is a simple ChatGPT clone built with Streamlit and OpenAI API. 
Ask me anything, and I'll respond like ChatGPT! 🤖
""")

# Creating the chat interface
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display the previous messages
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**ChatGPT:** {message['content']}")

# Get user input
user_input = st.text_input("You:", "")

if user_input:
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get ChatGPT's response
    chatgpt_response = get_openai_response(st.session_state.messages)

    # Add ChatGPT's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": chatgpt_response})

    # Scroll to the bottom of the chat
    st.experimental_rerun()

# Optional: Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
    st.experimental_rerun()
