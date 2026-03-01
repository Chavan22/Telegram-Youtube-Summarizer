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
