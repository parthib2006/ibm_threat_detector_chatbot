import streamlit as st
from ruleset import detect_threats

st.set_page_config(page_title="Cyber Threat Chatbot", page_icon="🛡️")
st.title("🛡️ Cyber Threat Detection Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Accept user input
user_input = st.chat_input("Paste a suspicious message or email...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Analyze input
    threats = detect_threats(user_input)

    # Prepare chatbot response
    if not threats:
        reply = "✅ No threats detected. This message looks safe."
    else:
        color_map = {
            "Phishing": "orange",
            "Scam": "red",
            "Abuse": "purple"
        }

        reply = "⚠️ **Threats Detected:**\n\n"
        for category, keywords in threats.items():
            joined_keywords = ", ".join(keywords)
            emoji = {
            "Phishing": "🟠",
            "Scam": "🔴",
            "Abuse": "🟣"
            }.get(category, "⚫")
            reply += f"- {emoji} **{category}**: {joined_keywords}\n"
        reply = reply.strip()

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(reply, unsafe_allow_html=True)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.caption('Project made by Team — The Cyber Researchers\nIBM SKILLSBUILD\nCSRBOX AI PBL')