# import whisper

# model = whisper.load_model("large")  # Use "large" for better accuracy

# result = model.transcribe("om.wav", task="translate", language="mr")


# print("Translated Text:", result["text"])




import speech_recognition as sr
def speech_to_text_from_file(audio_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        print("Processing audio file...")
        audio = recognizer.record(source)  # Read the entire audio file
    try:
        text = recognizer.recognize_google(audio)  # Using Google API
        print("Recognized Text:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")

# Provide your audio file path
audio_file_path = "harvard.wav"  # Ensure it's in WAV format
speech_to_text_from_file(audio_file_path)
