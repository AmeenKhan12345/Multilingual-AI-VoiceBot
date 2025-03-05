# Multilingual AI Voice Bot

**Multilingual AI Voice Bot** is an advanced, real-time speech-to-speech communication system that integrates state-of-the-art AI technologies to enable seamless multilingual interactions. It uses **Whisper AI** for speech recognition, **OpenAI GPT-3.5 Turbo** for generating context-aware responses, and **Google Cloud Text-to-Speech** (TTS) for natural speech output. Additionally, it incorporates **audio steganography** to ensure tamper-proof and secure audio communication.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Key Technologies](#key-technologies)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

Our **Multilingual AI Voice Bot** enables users to interact through real-time voice commands. The system:
- **Transcribes speech** using Whisper AI.
- **Generates natural responses** with OpenAI GPT-3.5 Turbo.
- **Converts text to speech** using Google Cloud TTS.
- **Secures audio communication** via audio steganography.

This solution enhances accessibility, overcomes language barriers, and offers a privacy-focused, interactive voice experience.

---

## Key Features

- **Real-Time Multilingual Communication:** Detects and responds in the user's language.
- **Dynamic Speech Detection:** Captures and processes voice input without a wake word.
- **AI-Powered Responses:** Generates context-aware replies using GPT-3.5 Turbo.
- **Secure Audio Output:** Embeds security watermarks through audio steganography.
- **Extensible:** Easily integrated as a browser extension or into smart devices.
- **User-Friendly Interface:** A Tkinter-based GUI displays conversation history seamlessly.

---

## Key Technologies

**AI Algorithms:**  
- Speech Recognition: *Whisper AI*  
- NLP & Response Generation: *OpenAI GPT-3.5 Turbo*  
- Text-to-Speech: *Google Cloud TTS*  
- Audio Steganography for security

**Programming Language:**  
- *Python*

**Frameworks & Libraries:**  
- *Tkinter* (GUI interface)  
- *SpeechRecognition* (audio capture)  
- *langdetect* (language detection)

**Real-Time Data Integration:**  
- Dynamic Speech Detection  
- Real-Time Audio Processing

**Other Technologies:**  
- Multilingual Support  
- Privacy & Security (audio steganography)

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/AI-VOICE-BOT.git
   cd AI-VOICE-BOT
2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Configure API Keys & Credentials:**
   Replace the placeholder OpenAI API key in app.py with your actual key.
   Place your Google Cloud service account JSON file in the appropriate location and update the file path in app.py.
5. **Run the Application:**
   ```bash
   python app.py
  The application will launch a Tkinter GUI for voice interaction.

## Usage
- **Voice Input:** Press the "Start Talking" button to record your voice. The bot dynamically captures your speech, transcribes it using Whisper, processes it via GPT-3.5 Turbo, and then responds using Google TTS.

- **Conversation History:** All user queries and bot responses are displayed in a scrollable text area, maintaining the conversation context.

## Future Enhancements
- **Enhanced Audio Steganography:** Further secure audio responses.
- **Advanced GUI:** Improve interface design and add more interactive features.
- **Edge Device Integration:** Adapt the solution for smart home assistants and IoT devices.
- **Extended API:** Expand backend functionalities for more nuanced conversation management.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

