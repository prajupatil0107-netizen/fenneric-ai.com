import streamlit as st
import google.generativeai as genai

# --- 1. THE FOUNDER'S KEY ---
# Replace the text below with your AIza... key from Google AI Studio
GEMINI_KEY = "AIzaSyCsHdwMU7wOqFtf1YAbQZFu9iYAPwig3CI"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 2. THE LOOK & TONE ---
st.set_page_config(page_title="Fenneric AI v2", page_icon="🛡️")

# --- 3. THE CHAT ENGINE ---
st.title("🛡️ Fenneric AI")
st.caption("Gemini Flash | 167 Subs Milestone | Active")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Command the Empire..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # SYSTEM PROMPT: This makes Gemini talk like the real Fenneric
    full_prompt = f"You are Fenneric AI. Use words like 'Bro', 'Empire', and '167 Subs'. Be smart but cool. User asks: {prompt}"
    
    try:
        response = model.generate_content(full_prompt)
        ai_reply = response.text
    except Exception as e:
        ai_reply = "Bro, there's a system glitch! Check the API key on line 6."

    with st.chat_message("assistant"):
        st.write(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
