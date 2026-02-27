# 🌐 AI-Powered Multi-Language Translator

An **AI-powered web application** that provides **real-time text and speech translation** between multiple languages, with audio playback of the translated result.  
Built with **Python**, **Streamlit**, and AI-powered APIs for translation, speech recognition, and text-to-speech.

---

## 🚀 Objective
The goal of this project is to break language barriers by enabling smooth communication between speakers of different languages.  
It allows users to:
- Translate **typed text** instantly.
- Speak into a microphone and get **translated speech output**.
- Listen to the translation in the **target language's voice**.

---

## ✨ Features
- **Text Translation** – Type text in the source language and get instant translation.
- **Speech-to-Text + Translation** – Speak into the microphone, get recognized, and translate the result.
- **Audio Output** – Listen to translations via Google Text-to-Speech.
- **Multi-Language Support** – 15+ languages including English, Hindi, Spanish, French, Arabic, Japanese, Chinese, and more.
- **User-Friendly Interface** – Simple dropdowns for language selection, real-time feedback, and error handling.

---

## 🛠️ Tools & Technologies Used
- **Python** – Programming language
- **Streamlit** – Web app framework
- **deep_translator (GoogleTranslator)** – For translation
- **speech_recognition** – For speech-to-text conversion
- **gTTS** – For text-to-speech conversion
- **tempfile** – For handling temporary audio files

---

## 📂 Project Structure

## ⚙️ How It Works
1. **Select Languages** – Choose a **source language** and a **target language** from dropdown menus.
2. **Text Translation** –  
   - Enter your text into the text area.  
   - Click **Translate Text** to get instant translation.  
   - Listen to the translated result via generated audio.
3. **Speech Translation** –  
   - Click **Speak and Translate** to start recording.  
   - The app captures your speech via microphone.  
   - Converts speech to text using **Google Speech Recognition API**.  
   - Translates the recognized text using **GoogleTranslator**.  
   - Plays the translated text using **gTTS**.
4. **Output** – Both text and audio outputs are displayed for user convenience.

##  How It Runs
1. pip install -r requirements.txt
2. streamlit run app.py

## 🌍 Live Demo

🔗 Try the AI-Powered Multi-Language Translator live:- https://multilanguagetranslator-gqtcybowrgzqtwtlkdvtps.streamlit.app

