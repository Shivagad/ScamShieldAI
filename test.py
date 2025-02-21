import joblib

# Load the trained model
model = joblib.load("best_fraud_detection_model.pkl")

# Example test messages
new_messages = [
    "Give me OTP",
    "Hello, how are you doing?",
    "Congratulations! You have won a $500 gift card. Claim now!"
]

# Predict fraud or normal
predictions = model.predict(new_messages)

# Show results
for msg, pred in zip(new_messages, predictions):
    print(f"📩 Message: {msg}")
    print(f"🔹 Prediction: {'Fraud' if pred == 1 else 'Normal'}\n")
