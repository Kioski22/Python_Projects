import whisper

model = whisper.load_model("tiny")
result = model.transcribe("/home/newadmin/Desktop/GMT20250530-105725_Recording.m4a")
with open("transcript_output.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("Transcript saved to transcript_output.txt")