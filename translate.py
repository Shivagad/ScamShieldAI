import whisper


model = whisper.load_model("base")

result = model.transcribe("om.wav", task="translate")


print("Translated Text:", result["text"])
