# 🌿 PlantDocBot – AI Plant Disease Diagnosis

PlantDocBot is a professional, AI-powered monolithic application for identifying plant diseases. It runs locally using **Streamlit** and combines offline Deep Learning models with online LLM capabilities to provide accurate diagnoses via **Image, Voice, or Text**.

---

## ✨ Key Features

### 1. 📷 Image Diagnosis (Offline / Local)

- **Model:** ResNet50 (PyTorch) trained on PlantVillage + PlantDoc datasets.
- **Function:** Upload a leaf image → Model predicts the disease class locally.
- **Classes:** Supports **28 classes** across **13+ crops** (Apple, Blueberry, Cherry, Corn, Grape, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato + Not_a_Plant rejection).
- **Features:** Shows top-3 prediction confidence percentages.

---

### 2. 🎤 Voice Assistant (Hybrid)

- **Transcription:** Uses **OpenAI Whisper (Local)** to transcribe speech to text on your device.
- **Analysis:** Uses **Groq API** to analyze the transcribed text and match it to known symptoms.
- **Requirements:** Requires `FFmpeg` installed on the system.

---

### 3. 💬 Text Diagnosis (Online)

- **Model:** **Groq API** (using `llama-3.3-70b-versatile`).
- **Function:** Semantic search matching user descriptions to the disease database.
- **UI:** Dedicated "Diagnose" button to prevent accidental API calls.

---

### 4. ⚙️ Smart UI/UX

- **Single-Mode Logic:** Only one diagnosis mode is active at a time to prevent confusion.
- **Dynamic Reset:** "🔄 New Diagnosis" completely wipes all state.
- **Light Theme:** Enforced professional white background via config.

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** PyTorch, ResNet50
- **AI / LLM:** Groq API
- **Speech Recognition:** OpenAI Whisper
- **Web Framework:** Streamlit
- **API Framework:** FastAPI
- **Datasets:** PlantVillage, PlantDoc
- **Additional Tools:** FFmpeg, Git, GitHub

---


## 🔄 How It Works

PlantDocBot supports three different diagnosis modes:

### 📷 Image Diagnosis

Upload a plant leaf image → Image preprocessing → ResNet50 model → Disease prediction → Confidence score → Disease information

### 🎤 Voice Diagnosis

Upload an audio file → OpenAI Whisper → Speech-to-text → Groq API → AI-generated response

### 💬 Text Diagnosis

Enter plant symptoms  → Groq API → Symptom analysis → AI-generated response

---

