import streamlit as st
import google.generativeai as genai
# 1. THE FOUNDER'S KEY (Line 6)
# Paste your NEW AIza key between the quotes below
GEMINI_KEY = "AIzaSyAQlclFXfd34ga1fZvXg-l-FNvxf03h3fc"

# 2. CONNECT TO THE BRAIN
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. THE INTERFACE LOOK
st.set_page_config(page_title="Fenneric AI v2", page_icon="🛡️")
st.title("🛡️ Fenneric AI")
st.caption("Gemini 3 Flash | 167 Subs Milestone | Active")

# 4. THE MEMORY BANK
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. SHOW PREVIOUS CHAT
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 6. THE COMMAND INPUT
if prompt := st.chat_input("Command the Empire..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # SYSTEM INSTRUCTION
    instruction = f"You are Fenneric AI, the digital general of the Fenneric Empire (167 Subs). Be cool, use 'Bro', and be smart. User says: {prompt}"
    
    try:
        response = model.generate_content(instruction)
        reply = response.text
    except Exception as e:
        reply = "Empire Error: Check the API Key in Line 6, Bro!"

    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
