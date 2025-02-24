import os
import joblib
import speech_recognition as sr
from flask import Flask, request, jsonify
from pydub import AudioSegment
from flask_cors import CORS
from transcribe_audio import transcribe_audio
from textpreprocess import expand_text
from preprocess_audio import preprocess_audio
import google.generativeai as genai  # Import Gemini API

app = Flask(__name__)
CORS(app)  # Allow all origins for all routes
CORS(app, origins=["https://scamshield-call.vercel.app"])

# Load trained model and vectorizer
loaded_model = joblib.load("finaltrainmodel.pkl")
loaded_vectorizer = joblib.load("vectorizer.pkl")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("Test Gemini API connection.")
# print(response.text)


def get_gemini_analysis(text):
    """
    Sends the transcript to Google Gemini API for fraud analysis.
    Returns a structured explanation and feedback.
    """
    prompt = (
        "You are a fraud detection AI analyzing phone call transcripts.\n"
        "Your task is to determine whether the conversation is suspicious or fraudulent.\n\n"
        "**Instructions:**\n"
        "- Identify signs of fraud (e.g., urgency, pressure, OTP requests, financial transactions).\n"
        "- Explain why the message is suspicious (if applicable).\n"
        "- Provide recommendations on how the recipient should respond.\n\n"
        "**Transcript Analysis:**\n"
        f"{text}\n\n"
        "**Response Format:**\n"
        "- **Fraud Risk (High / Medium / Low):** [Your assessment]\n"
        "- **Reasoning:** [Explain why this might be fraudulent]\n"
        "- **Red Flags Detected:** [List key words, tone, or behaviors that indicate fraud]\n"
        "- **Advice for Recipient:** [How should the person react to this message?]\n"
    )

    try:
        response = model.generate_content(prompt)
        return response.text  # Extracts text response from Gemini
    except Exception as e:
        return f"Error analyzing with Gemini: {str(e)}"



@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    audio_path = f"temp_audio.{file.filename.split('.')[-1]}"
    file.save(audio_path)

    # Process audio
    clean_audio_path = preprocess_audio(audio_path)
    text = transcribe_audio(clean_audio_path)
    text = expand_text(text)
    print(text)
    
    os.remove(audio_path)

    if text in ["Could not understand audio", "Speech Recognition API unavailable"]:
        return jsonify({"error": text}), 400

    # Vectorize text and get model prediction
    text_vectorized = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(text_vectorized)[0]

    # Get detailed Gemini analysis
    gemini_analysis = get_gemini_analysis(text)
    print(gemini_analysis)

    return jsonify({
        "prediction": "Fraud" if prediction == 1 else "Normal",
        "transcription": text,
        "gemini_analysis": gemini_analysis
    })

if __name__ == "__main__":
    app.run(debug=True)
