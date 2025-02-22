
import os
import joblib
import speech_recognition as sr
from flask import Flask, request, jsonify
from pydub import AudioSegment
from flask_cors import CORS 
from transcribe_audio import transcribe_audio
from textpreprocess import expand_text
from preprocess_audio import preprocess_audio

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow all origins for /predict

loaded_model = joblib.load("finaltrainmodel.pkl")
loaded_vectorizer = joblib.load("vectorizer.pkl")


def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    
    if not audio_path.endswith(".wav"):
        sound = AudioSegment.from_file(audio_path)
        audio_path = audio_path.replace(audio_path.split(".")[-1], "wav")
        sound.export(audio_path, format="wav")

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech Recognition API unavailable"


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    audio_path = f"temp_audio.{file.filename.split('.')[-1]}"
    file.save(audio_path)
    # text = audio_to_text(audio_path)
    clean_audio_path=preprocess_audio(audio_path)
    text = transcribe_audio(clean_audio_path)
    print(text)
    text = expand_text(text)
    print(text)
    os.remove(audio_path)
    if text in ["Could not understand audio", "Speech Recognition API unavailable"]:
        return jsonify({"error": text}), 400

    
    text_vectorized = loaded_vectorizer.transform([text])

    prediction = loaded_model.predict(text_vectorized)[0]

    return jsonify({"prediction": "Fraud" if prediction == 1 else "Normal", "transcription": text})

if __name__ == "__main__":
    app.run(debug=True)
