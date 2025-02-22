import whisper

# Load Whisper model once (Global)
model = whisper.load_model("small")

def transcribe_audio(audio_path):
    """Transcribes and translates an audio file using Whisper with auto language detection."""
    result = model.transcribe(audio_path, task="translate")  # No language parameter for auto-detect
    return result["text"]  # Extract translated text
