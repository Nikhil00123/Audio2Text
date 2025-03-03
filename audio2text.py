import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe(r"C:\Users\rajes\OneDrive\Desktop\audio2text\harvard.wav")
print(result["text"])

