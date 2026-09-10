"""
🤖 Rule-Based ChatBot — Streamlit Edition
A colorful, interactive chat interface for a simple rule-based chatbot.

Run with:
    streamlit run app.py
"""

import streamlit as st
import time
from datetime import datetime

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# CUSTOM CSS — colour grading & styling
# ----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00c6ff, #92fe9d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #b8c6db;
        font-size: 1rem;
        margin-top: 0px;
        margin-bottom: 1.2rem;
    }

    /* Chat bubbles */
    div[data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 4px 8px;
        margin-bottom: 6px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    }

    /* Metric cards in sidebar */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 12px 6px;
        border-radius: 14px;
    }
    div[data-testid="stMetricLabel"] { color: #92fe9d !important; font-weight: 600; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1c1c3c 0%, #2b2b52 100%);
    }
    section[data-testid="stSidebar"] * { color: #f1f1f1 !important; }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #92fe9d);
        color: #0f2027;
        font-weight: 700;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1.1rem;
        transition: 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 15px rgba(146, 254, 157, 0.5);
    }

    /* Chat input box */
    .stChatInput textarea {
        border-radius: 12px !important;
    }

    hr { border-color: rgba(255,255,255,0.15); }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# RESPONSES KNOWLEDGE BASE
# ----------------------------------------------------------------------------
RESPONSES = {
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hello! How can I help you?",
    "hey": "Hey! How can I assist you?",
    "good morning": "Good morning! Have a great day.",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! What can I do for you?",
    "good night": "Good night! Sleep well.",
    "how are you": "I'm doing great! How about you?",
    "how are you doing": "I'm doing well. Thanks for asking!",
    "what's up": "Not much! How can I help?",

    # Identity
    "who are you": "I am a rule-based chatbot built in Python.",
    "what are you": "I am an AI chatbot.",
    "what is your name": "My name is ChatBot.",
    "tell me your name": "I'm ChatBot.",
    "who made you": "I was created using Python.",
    "who created you": "A Python developer created me.",
    "are you human": "No, I am a chatbot.",
    "are you a robot": "Yes, you can think of me as a virtual assistant.",
    "what can you do": "I can answer your questions and assist you.",
    "what is your purpose": "My purpose is to help users with their questions.",

    # Help
    "help": "Sure! Tell me what you need.",
    "can you help me": "Of course! What do you need help with?",
    "i need help": "I'm here to help.",
    "support": "Please tell me your problem.",
    "assist me": "Sure! What do you need assistance with?",

    # Time & Date
    "what time is it": "You can use Python's datetime module to get the current time.",
    "tell me the time": "Use datetime.now().strftime('%H:%M:%S') in Python.",
    "what is today's date": "Use datetime.date.today() in Python.",
    "today's date": "Today's date can be obtained using Python datetime.",
    "what day is today": "You can check today's weekday using Python datetime.",

    # Weather
    "what is the weather": "Sorry, I cannot access live weather.",
    "how is the weather": "I can't check live weather.",
    "is it raining": "I don't have live weather updates.",
    "weather today": "Please check a weather app.",

    # Basic Conversation
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "thank you so much": "My pleasure!",
    "bye": "Goodbye! Have a nice day.",
    "goodbye": "See you later!",
    "see you": "Take care!",
    "catch you later": "Bye! Have a great day.",
    "talk to you later": "Looking forward to it!",
    "ok": "Alright!",
    "okay": "Okay!",
    "fine": "Glad to hear that.",
    "cool": "Great!",
    "awesome": "That's awesome!",
    "nice": "Glad you think so!",

    # Personal
    "where do you live": "I live inside your computer.",
    "where are you from": "I was created in Python.",
    "how old are you": "I don't have an age.",
    "do you have friends": "I make new friends every day.",
    "do you sleep": "No, I work 24/7.",
    "are you married": "No.",
    "do you love me": "I appreciate our conversation!",
    "can we be friends": "Of course!",
    "do you eat": "No, I don't need food.",
    "what is your favorite food": "Electricity!",
    "what is your favorite color": "Blue.",
    "what is your favorite movie": "I enjoy science fiction.",
    "what is your hobby": "Helping users.",

    # Programming
    "what is python": "Python is a high-level programming language.",
    "what is java": "Java is an object-oriented programming language.",
    "what is c": "C is a procedural programming language.",
    "what is c++": "C++ is an extension of C supporting OOP.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS styles web pages.",
    "what is javascript": "JavaScript adds interactivity to websites.",
    "what is sql": "SQL is used to manage databases.",
    "what is machine learning": "Machine Learning enables computers to learn from data.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is chatbot": "A chatbot is software that interacts with users through conversation.",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me something funny": "Debugging is like being a detective in a crime movie where you are also the murderer.",
    "make me laugh": "There are only 10 types of people: those who understand binary and those who don't.",
    "do you know jokes": "Yes! Ask me to tell you one.",
    "sing a song": "Sorry, I can't sing.",
    "dance": "I can dance in binary!",
    "flip a coin": "Heads!",
    "roll a dice": "You rolled a 4!",

    # Math
    "what is 2+2": "4",
    "what is 10+20": "30",
    "what is pi": "Pi is approximately 3.14159.",
    "what is square root": "The square root of a number is a value that when multiplied by itself gives the original number.",

    # Internet
    "what is google": "Google is a search engine.",
    "what is youtube": "YouTube is a video sharing platform.",
    "what is github": "GitHub is a platform for hosting code.",
    "what is wikipedia": "Wikipedia is a free online encyclopedia.",

    # General Knowledge
    "what is india": "India is a country in South Asia.",
    "who is the president of india": "I may not have updated information.",
    "what is the capital of india": "New Delhi.",
    "largest ocean": "The Pacific Ocean.",
    "highest mountain": "Mount Everest.",
    "fastest animal": "The Peregrine Falcon is the fastest animal.",
    "largest planet": "Jupiter.",
    "smallest planet": "Mercury.",
    "who invented python": "Python was created by Guido van Rossum.",
    "who invented the telephone": "Alexander Graham Bell.",

    # Emotions
    "i am happy": "That's wonderful!",
    "i am sad": "I'm sorry to hear that.",
    "i am bored": "Maybe try learning something new!",
    "i am tired": "Take some rest.",
    "i am stressed": "Remember to take breaks and relax.",

    # Common Requests
    "open google": "Sorry, I cannot open applications.",
    "play music": "Sorry, I cannot play music.",
    "open youtube": "I cannot open websites directly.",
    "search for python": "I cannot search the web.",
    "calculate": "Please enter a mathematical expression.",
}

QUICK_REPLIES = [
    "hello", "tell me a joke", "what is python",
    "what can you do", "flip a coin", "bye",
]


def bot_response(user_text: str) -> str:
    text = user_text.lower()
    for key in RESPONSES:
        if key in text:
            return RESPONSES[key]
    return "Out of bound question 🤔 — try rephrasing, or type **help** to see what I can do."


# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hello! Welcome to the rule-based chatbot system 🤖\nType your message below, or try one of the quick replies in the sidebar!",
         "time": datetime.now().strftime("%H:%M")}
    ]

if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False

# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
st.markdown('<div class="main-title">🤖 Rule-Based ChatBot</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ask me about programming, general knowledge, jokes, and more!</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    st.header("📊 Chat Stats")
    user_msgs = [m for m in st.session_state.messages if m["role"] == "user"]
    bot_msgs = [m for m in st.session_state.messages if m["role"] == "assistant"]
    unanswered = [m for m in bot_msgs if "Out of bound" in m["content"]]

    c1, c2 = st.columns(2)
    c1.metric("💬 Your Messages", len(user_msgs))
    c2.metric("🤖 Bot Replies", len(bot_msgs))
    st.metric("❓ Unanswered", len(unanswered))

    st.markdown("---")
    st.header("⚡ Quick Replies")
    st.caption("Tap to instantly send a message")
    for q in QUICK_REPLIES:
        if st.button(q, key=f"quick_{q}", use_container_width=True):
            st.session_state["pending_input"] = q

    st.markdown("---")
    st.header("🧠 Knowledge Base")
    st.caption(f"I currently know **{len(RESPONSES)}** phrases across topics like greetings, programming, fun facts, math, and more.")

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat cleared! How can I help you now?",
             "time": datetime.now().strftime("%H:%M")}
        ]
        st.session_state.chat_ended = False
        st.rerun()

# ----------------------------------------------------------------------------
# CHAT DISPLAY
# ----------------------------------------------------------------------------
for msg in st.session_state.messages:
    avatar = "🤖" if msg["role"] == "assistant" else "🧑"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
        st.caption(msg.get("time", ""))

# ----------------------------------------------------------------------------
# HANDLE INPUT (either typed or a quick-reply button)
# ----------------------------------------------------------------------------
typed_input = None
if not st.session_state.chat_ended:
    typed_input = st.chat_input("Type your message here...")

pending = st.session_state.pop("pending_input", None)
user_text = pending or typed_input

if user_text and not st.session_state.chat_ended:
    now = datetime.now().strftime("%H:%M")
    st.session_state.messages.append({"role": "user", "content": user_text, "time": now})

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_text)
        st.caption(now)

    reply = bot_response(user_text)

    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        typed = ""
        for ch in reply:
            typed += ch
            placeholder.markdown(typed + "▌")
            time.sleep(0.01)
        placeholder.markdown(typed)
        st.caption(datetime.now().strftime("%H:%M"))

    st.session_state.messages.append(
        {"role": "assistant", "content": reply, "time": datetime.now().strftime("%H:%M")}
    )

    if "bye" in user_text.lower():
        st.session_state.chat_ended = True
        st.balloons()
        st.rerun()

if st.session_state.chat_ended:
    st.success("Thanks for using our bot! 👋 Click **Clear Chat** in the sidebar to start a new conversation.")

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#888;'>Made with ❤️ using Streamlit</div>",
    unsafe_allow_html=True,
)
