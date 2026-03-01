# Telegram YouTube Summarizer Bot

A Telegram bot that summarizes YouTube videos using a locally hosted Large Language Model via Ollama.

Unlike cloud-based solutions, this project runs LLM inference locally, ensuring:
- No external API dependency
- Lower cost
- Better privacy
- Full control over model execution

---

## Overview

Users send a YouTube link to the Telegram bot.  
The system:

1. Extracts transcript from the video  
2. Processes and cleans the text  
3. Sends it to a locally running LLM (via Ollama)  
4. Returns a concise summary to Telegram  

This project demonstrates real-world backend engineering with local AI model deployment.

---

## Features

- Automatic YouTube transcript extraction
- Local LLM-based summarization (Ollama)
- Telegram bot integration
- Fast response time
- Privacy-friendly (no external LLM APIs)
- Robust error handling

---

## System Architecture

User  
   ↓  
Telegram Bot  
   ↓  
YouTube Transcript API  
   ↓  
Ollama (Local LLM)  
   ↓  
Generated Summary  
   ↓  
Telegram Response  

---

## Tech Stack

- Python
- Ollama (Local LLM Runtime)
- YouTube Transcript API
- Telegram Bot API
- Virtual Environment (venv)

---

```
telegram-youtube-summarizer/
│
├── bot.py
├── summarizer.py
├── test_transcript.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
---

## Setup Instructions

### 1️⃣ Install Ollama

Download and install Ollama from the official website.
https://ollama.com/download

Start Ollama:
```bash
ollama serve
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/telegram-youtube-summarizer.git
cd telegram-youtube-summarizer
```

### 3️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate # for Mac/Linux
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Bot
```bash
python bot.py
```

### Example Usage
**Try the bot here:**
Open Telegram
https://t.me/@VideoInsightsBot

Open the link above  
Click **Start**  
Send a YouTube video link  
Receive a structured summary generated locally by the LLM

User can ask multiple follow-up questions like 
1. summarize video in Hindi/ Kannada,
2. Practical action points from the transcript,
3. provide detailed explaination,
4. Ask anything related to Video, etc..,
