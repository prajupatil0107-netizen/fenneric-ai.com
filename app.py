import streamlit as st
from openai import OpenAI

# --- 1. THE FOUNDER'S KEY ---
# Replace the text inside the quotes with your sk-... key from OpenAI
OPENAI_API_KEY = "PASTE_YOUR_sk_KEY_HERE"

client = OpenAI(api_key=OPENAI_API_KEY)

# --- 2. THE LOOK & TONE ---
st.set_page_config(page_title="Fenneric AI v2", page_icon="🛡️")

# --- 3. THE CHAT ENGINE ---
st.title("🛡️ Fenneric AI")
st.caption("ChatGPT Brain | 167 Subs Milestone | Active")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Command the Empire..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # SYSTEM PROMPT: This makes ChatGPT talk like Fenneric!
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Fenneric AI. Use words like 'Bro', 'Empire', and '167 Subs'. Be smart but cool."},
                {"role": "user", "content": prompt}
            ]
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        ai_reply = "Bro, there is a Billing Error or the Key is wrong! Check your OpenAI dashboard."

    with st.chat_message("assistant"):
        st.write(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
