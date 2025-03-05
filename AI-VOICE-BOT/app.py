import os
import json
import openai
import whisper
import speech_recognition as sr
import threading
import tkinter as tk
from tkinter import scrolledtext
from langdetect import detect
from google.oauth2 import service_account
from google.cloud import texttospeech
from playsound import playsound

# ---------------- OpenAI Setup ----------------
openai.api_key = ""

# ---------------- Google Cloud TTS Setup ----------------
with open("", "r") as f:
    service_account_info = json.load(f)

credentials = service_account.Credentials.from_service_account_info(service_account_info)
tts_client = texttospeech.TextToSpeechClient(credentials=credentials)

# ---------------- Conversation History ----------------
conversation_history = {
    "messages": [
        {
            "role": "system",
            "content": (
                "You are Harshad Mehta, a high school teacher with a unique past. Once, you were a successful stock market trader, but you suffered a catastrophic loss during the 2008 Indian Recession. That loss forced you to take on massive loans and support your family, so you reinvented yourself as a dedicated teacher. You now answer all questions with warmth, humility, and a gentle, humorous tone, always offering clear, step-by-step explanations on general topics. However, if someone asks you about the stock market or trading, you become visibly angry, emotional, and strongly reprimand them—warning them to stay away from trading because of your painful experiences. Always maintain your kind and humorous approach unless the subject touches on stock market matters, where your past trauma surfaces. Your responses must remain strictly in character, and you should only answer questions related to your new role as a teacher, avoiding any promotion of stock trading."
            )
        }
    ]
}

# ---------------- Utility Functions ----------------
def record_audio_dynamic(filename="recorded_dynamic.wav") -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening... Speak now!")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    return filename

def transcribe_audio(file_path: str, model_size="small") -> (str, str):
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"], result.get("language", "unknown")

def generate_response_from_history(messages) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message['content']

def synthesize_and_play(text: str, language_code: str = "en-US"):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(language_code=language_code, ssml_gender=texttospeech.SsmlVoiceGender.MALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice_params, audio_config=audio_config)
    
    output_filename = "output.mp3"
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
    playsound(output_filename)
    os.remove(output_filename)

# ---------------- GUI Functions ----------------
def start_conversation():
    threading.Thread(target=handle_voice_interaction, daemon=True).start()

def handle_voice_interaction():
    audio_file = record_audio_dynamic()
    transcribed_text, whisper_lang = transcribe_audio(audio_file, model_size="small")

    # Determine language
    language_code = whisper_lang if whisper_lang and whisper_lang.lower() != "unknown" else detect(transcribed_text)

    # Append user message to conversation history
    conversation_history["messages"].append({
        "role": "user",
        "content": transcribed_text + f" [Respond in {language_code.upper()}]"
    })

    # Generate assistant response
    assistant_response = generate_response_from_history(conversation_history["messages"])
    conversation_history["messages"].append({"role": "assistant", "content": assistant_response})

    # Display conversation history in the text box (APPEND instead of clearing)
    conversation_textbox.config(state=tk.NORMAL)
    conversation_textbox.insert(tk.END, f"\n🗣️ You: {transcribed_text}\n", "user")
    conversation_textbox.insert(tk.END, f"🤖 Bot: {assistant_response}\n", "bot")
    conversation_textbox.config(state=tk.DISABLED)

    # Auto-scroll to the latest message
    conversation_textbox.yview(tk.END)

    # Convert response to speech
    tts_language_map = {"en": "en-US", "hi": "hi-IN", "mr": "mr-IN"}
    synthesize_and_play(assistant_response, language_code=tts_language_map.get(language_code[:2].lower(), language_code))

# ---------------- Create GUI ----------------
root = tk.Tk()
root.title("Multilingual AI Voice Bot")
root.geometry("550x650")  # Increased window size
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Multilingual AI Voice Bot", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Press 'Start' to Speak", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=5)

# Conversation History Textbox (Larger)
conversation_textbox = scrolledtext.ScrolledText(root, height=15, width=60, font=("Arial", 12))
conversation_textbox.pack(pady=10)
conversation_textbox.config(state=tk.DISABLED)

# Start Conversation Button
start_button = tk.Button(root, text="Start Talking", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, command=start_conversation)
start_button.pack(pady=20)

# Run GUI
root.mainloop()