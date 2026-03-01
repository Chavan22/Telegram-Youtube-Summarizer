# from youtube_transcript_api import YouTubeTranscriptApi
# import re

# def extract_video_id(url):
#     pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
#     match = re.search(pattern, url)
#     if match:
#         return match.group(1)
#     return None

# def get_transcript(url):
#     video_id = extract_video_id(url)
#     if not video_id:
#         raise ValueError("Invalid YouTube URL")

#     transcript = YouTubeTranscriptApi.get_transcript(video_id)

#     full_text = ""
#     for entry in transcript:
#         full_text += f"[{int(entry['start'])} sec] {entry['text']} "

#     return full_text


import yt_dlp
import whisper
import os

model = whisper.load_model("base")  # small model


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir():
        if file.startswith("audio"):
            return file

    raise Exception("Audio download failed.")


def get_transcript(url):
    audio_file = download_audio(url)

    result = model.transcribe(audio_file)

    os.remove(audio_file)

    return result["text"]