import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Grok Chatbot", page_icon="🤖")
st.title("🤖 Grok jaisa Chatbot")
st.caption("xAI ke Grok model se powered • Truthful aur helpful answers")

# API Key handling (robust: secrets ya input)
try:
    # Deploy pe secrets se lega
    api_key = st.secrets["XAI_API_KEY"]
except:
    # Local test ke liye input
    api_key = st.text_input("xAI API Key daalo:", type="password")
    if not api_key:
        st.info("API key daalo taake chatbot chalay. Key yahan se lo: https://console.x.ai")
        st.stop()

# Client banao
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are Grok, a maximally truth-seeking AI built by xAI. "
                       "Be helpful, witty when appropriate, and always give accurate answers. "
                       "Do not mention that you are an AI unless asked."
        }
    ]

# Purani messages display karo
for message in st.session_state.messages[1:]:  # system skip
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Kuch bhi poocho..."):
    # User message add aur display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model="grok-4-1-fast-reasoning",  # Latest fast + reasoning model (2M context)
                messages=st.session_state.messages,
                stream=True,
                temperature=0.8,
                max_tokens=2048,
            )
            # Streaming response
            response = st.write_stream(
                (chunk.choices[0].delta.content or "") for chunk in stream
            )
        except Exception as e:
            st.error(f"Error aa gaya: {str(e)}")
            response = "Sorry, kuch issue hai. Dobara try karo ya API key check karo."

    # Response history me save karo
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar me clear chat button
with st.sidebar:
    st.header("Options")
    if st.button("Chat clear karo"):
        st.session_state.messages = [st.session_state.messages[0]]  # Sirf system prompt rakh
        st.rerun()

    st.caption("Model: grok-4-1-fast-reasoning (latest aur fast)")
    st.caption("Note: API usage ka bill xAI se aayega (bohat sasta hai fast model).")
