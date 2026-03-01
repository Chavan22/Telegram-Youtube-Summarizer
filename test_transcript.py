from youtube_transcript_api import YouTubeTranscriptApi

video_id = "dQw4w9WgXcQ"  # test video

transcript = YouTubeTranscriptApi.get_transcript(video_id)

print("Transcript length:", len(transcript))