import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocess_audio import preprocess_audio
from transcribe_audio import transcribe_audio

app = Flask(__name__)
CORS(app)

# Load trained model and vectorizer
loaded_model = joblib.load("finaltrainmodel.pkl")
loaded_vectorizer = joblib.load("vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    audio_path = f"temp_audio.{file.filename.split('.')[-1]}"
    file.save(audio_path)

    # Step 1: Preprocess (Noise Reduction)
    cleaned_audio_path = preprocess_audio(audio_path)

    # Step 2: Transcribe & Translate
    text = transcribe_audio(cleaned_audio_path)
    
    # Cleanup temporary files
    os.remove(audio_path)
    os.remove(cleaned_audio_path)

    if not text.strip():
        return jsonify({"error": "Could not understand audio"}), 400

    # Step 3: Vectorize & Predict
    text_vectorized = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(text_vectorized)[0]

    return jsonify({"prediction": "Fraud" if prediction == 1 else "Normal", "transcription": text})

if __name__ == "__main__":
    app.run(debug=True)
