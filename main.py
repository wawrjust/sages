import streamlit as st
import openai


def ask_ai(messages):
    print(messages)
    return "Response from AI"


st.title("Streamlit AI Chatbot")
st.subheader("Streamlit AI")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Co to jest wrona?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    ai_response = ask_ai(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.chat_message("assistant").write(ai_response)


