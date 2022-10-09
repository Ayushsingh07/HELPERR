from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript("ZXiruGOCn9s")

text = ""
with open("file.txt", "w") as file:
  for i in srt:
    text += i["text"] + " "
  file.write(text)
