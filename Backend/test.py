import joblib
import numpy as np
from sklearn import metrics

# *✅ Load Saved Model & Vectorizer*
model = joblib.load("finaltrainmodel.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("\n🚀 Scam Detection Model Loaded Successfully!")

# *✅ Interactive Loop*
while True:
    # Get user input
    user_input = input("\n📩 Enter a message to classify (or type 'exit' to quit): ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("🔴 Exiting... Goodbye! 👋")
        break

    input_vectorized = vectorizer.transform([user_input])
    prediction = model.predict(input_vectorized)[0]

    label = "🚨 Fraud" if prediction == 1 else "✅ Not a Fraud"
    print(f"🎯 Prediction: {label}")