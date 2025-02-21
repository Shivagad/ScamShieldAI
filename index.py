from flask import Flask, request, jsonify
from flask_cors import CORS
from pydub import AudioSegment
from pydub.effects import normalize
import noisereduce as nr
import librosa
import soundfile as sf
import whisper
from transformers import pipeline

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Predefined scam keywords
SCAM_KEYWORDS = [
    "otp", "cvv", "install anydesk", "install teamviewer", "bank account",
    "verification code", "credit card", "debit card", "pin", "account number",
    "identity verification", "login credentials", "password reset", 
    "security update", "unauthorized transaction", "fraudulent transaction",
    "suspicious activity", "government investigation", "customs", "irs", 
    "income tax", "arrest warrant", "legal action", "block your account",
    "freeze your account", "insurance claim", "loan approval", "credit score",
    "investment opportunity", "lottery winnings", "prize money", 
    "immediate payment", "urgent payment", "money transfer", "gift card",
    "paypal login", "amazon account", "google account", "microsoft account",
    "remote assistance", "remote desktop", "data breach", "identity theft",
    "social security number", "compromised account", "malware installation",
    "update software", "ransomware", "financial assistance", "donation request"
]

# Load pre-trained sentiment model for additional rule-based checking
sentiment_pipeline = pipeline("sentiment-analysis")

# Preprocess audio: convert to mono, normalize, noise reduce, and resample to 16kHz
def preprocess_audio(input_audio_path, output_audio_path):
    print("Preprocessing audio...")
    # Load and convert audio to mono using pydub
    audio = AudioSegment.from_file(input_audio_path).set_channels(1)
    # Normalize the audio
    audio = normalize(audio)
    # Export intermediate normalized audio file
    intermediate_file = "normalized_audio.wav"
    audio.export(intermediate_file, format="wav")
    
    # Load normalized audio using librosa and resample to 16kHz
    y, sr = librosa.load(intermediate_file, sr=16000)
    # Apply noise reduction using noisereduce
    y_denoised = nr.reduce_noise(y=y, sr=sr)
    # Save final processed audio using soundfile
    sf.write(output_audio_path, y_denoised, sr)
    print("Audio preprocessing completed.")

# Load Whisper model globally (to speed up subsequent requests)
whisper_model = whisper.load_model("base")

# Transcribe audio using Whisper with translation (if needed)
def transcribe_audio(audio_path):
    print("Transcribing audio using Whisper...")
    result = whisper_model.transcribe(audio_path, task="translate")
    text = result["text"]
    print("Transcription completed.")
    return text

# Simple keyword and sentiment-based classifier for suspicious activity
def detect_suspicious_activity(transcript):
    if not transcript:
        return "Not Suspicious", "Could not process audio"
    
    # Check for scam keywords (case-insensitive)
    transcript_lower = transcript.lower()
    keyword_matches = [word for word in SCAM_KEYWORDS if word in transcript_lower]
    
    # Perform sentiment analysis on the transcript
    sentiment_result = sentiment_pipeline(transcript)[0]
    is_aggressive = sentiment_result['label'] == "NEGATIVE" and sentiment_result['score'] > 0.8
    
    # Rule-based classification
    if keyword_matches or is_aggressive:
        reason = ("Mentioned keywords: " + ", ".join(keyword_matches)
                  if keyword_matches else "High aggression in tone")
        return "Suspicious", reason
    else:
        return "Not Suspicious", "No scam indicators detected."

# Flask route for uploading the audio file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file:
        # Save the uploaded file temporarily
        file_path = "uploaded_audio.wav"
        file.save(file_path)
        
        # Preprocess the audio file
        final_audio_path = "final_audio.wav"
        preprocess_audio(file_path, final_audio_path)
        
        # Transcribe the preprocessed audio using Whisper
        transcript = transcribe_audio(final_audio_path)
        
        # Classify the transcript as Suspicious or Not Suspicious
        label, reason = detect_suspicious_activity(transcript)
        
        return jsonify({"label": label, "reason": reason, "transcript": transcript})

    return jsonify({"error": "Invalid file"}), 400

if __name__ == '__main__':
    app.run(debug=True)
