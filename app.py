import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr
from gtts import gTTS
import tempfile
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Powered Translator", layout="wide", page_icon="🌐")

# --- ADVANCED CSS ---
st.markdown("""
    <style>
    /* Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Title Styling */
    .main-title {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        color: white;
        text-shadow: 3px 3px 15px rgba(0,0,0,0.4);
        padding-top: 10px;
    }

    /* Input & Result Boxes */
    .stTextArea textarea {
        background: white !important;
        color: #1a202c !important; 
        font-size: 18px !important;
        border-radius: 15px !important;
    }

    .stAlert {
        background-color: white !important;
        color: #000000 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border-left: 12px solid #e73c7e !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background: white;
        color: #e73c7e !important;
        font-weight: bold;
        transition: 0.4s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: #e73c7e;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 50+ LANGUAGES ---
lang_map = {
    "English": "en", "Hindi": "hi", "Marathi": "mr", "Gujarati": "gu", "Punjabi": "pa",
    "Bengali": "bn", "Tamil": "ta", "Telugu": "te", "Kannada": "kn", "Malayalam": "ml",
    "Urdu": "ur", "Sanskrit": "sa", "French": "fr", "German": "de", "Spanish": "es",
    "Italian": "it", "Portuguese": "pt", "Russian": "ru", "Japanese": "ja", "Korean": "ko",
    "Chinese (Simplified)": "zh-CN", "Arabic": "ar", "Turkish": "tr", "Vietnamese": "vi",
    "Thai": "th", "Indonesian": "id", "Dutch": "nl", "Greek": "el", "Hebrew": "he",
    "Persian": "fa", "Polish": "pl", "Romanian": "ro", "Swedish": "sv", "Danish": "da",
    "Finnish": "fi", "Norwegian": "no", "Czech": "cs", "Hungarian": "hu", "Ukrainian": "uk",
    "Malay": "ms", "Filipino": "tl", "Afrikaans": "af", "Amharic": "am", "Azerbaijani": "az",
    "Belarusian": "be", "Bulgarian": "bg", "Catalan": "ca", "Croatian": "hr", "Estonian": "et",
    "Irish": "ga", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Slovak": "sk"
}

# --- HEADER ---
st.markdown("<h1 class='main-title'>AI Powered Multi-Language Translator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Breaking Language Barriers with Intelligence</p>", unsafe_allow_html=True)

# --- SELECTION AREA ---
languages = sorted(list(lang_map.keys()))
col1, col2, col3 = st.columns([2, 0.5, 2])
with col1:
    src_name = st.selectbox("📥 From Language", languages, index=languages.index("English"))
with col2:
    st.markdown("<h2 style='text-align:center; margin-top:20px;'>⇄</h2>", unsafe_allow_html=True)
with col3:
    tar_name = st.selectbox("📤 To Language", languages, index=languages.index("Hindi"))

src_code = lang_map[src_name]
tar_code = lang_map[tar_name]

st.markdown("---")

# --- MAIN CONTENT ---
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown("### ✍️ Text Translation")
    input_text = st.text_area("Enter your text here...", height=150)
    
    if st.button("Translate Text ✨"):
        if input_text.strip():
            with st.spinner('Translating...'):
                translated = GoogleTranslator(source=src_code, target=tar_code).translate(text=input_text)
                st.snow()
                st.markdown("#### **Result:**")
                st.success(translated)
                
                try:
                    tts = gTTS(text=translated, lang=tar_code)
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                        tts.save(f.name)
                        st.audio(f.name)
                except: pass

with right_col:
    st.markdown("### 🎤 Voice Translation")
    st.write("Click, speak, and watch the magic!")
    
    if st.button("Speak & Translate 🎧"):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                st.toast("Listening... Speak now!", icon="🎙️")
                audio = recognizer.listen(source, timeout=5)
                spoken = recognizer.recognize_google(audio, language=src_code)
                st.info(f"You said: {spoken}")
                
                translated_v = GoogleTranslator(source=src_code, target=tar_code).translate(text=spoken)
                st.balloons()
                st.markdown("#### **Result:**")
                st.success(translated_v)
                
                tts = gTTS(text=translated_v, lang=tar_code)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                    tts.save(f.name)
                    st.audio(f.name)
        except:
            st.error("Could not process voice. Check mic or PyAudio.")

st.markdown("<br><p style='text-align:center; opacity:0.8; color:white;'>Supporting 50+ Global Languages</p>", unsafe_allow_html=True)