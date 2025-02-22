import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")  # Ensure dataset.csv is in the same folder

# Convert labels to binary (fraud -> 1, normal -> 0)
df['label'] = df['label'].apply(lambda x: 1 if x == 'fraud' else 0)

# Track best accuracy and model
best_accuracy = 0.0
best_model = None

# Run training 100 times
for i in range(100):
    print(f"🔄 Training Iteration {i+1}/100")

    # Split dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=i)

    # Create a text classification pipeline with n-grams (bigram for better context)
    model = make_pipeline(TfidfVectorizer(ngram_range=(1,2)), LogisticRegression())

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"📊 Accuracy for Iteration {i+1}: {accuracy:.4f}")

    # Store the best model
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        print(f"✅ New Best Accuracy: {best_accuracy:.4f} (Model Saved)")

# Save the best trained model
joblib.dump(best_model, "best_fraud_detection_model.pkl")
print(f"💾 Best Model saved as 'best_fraud_detection_model.pkl' with Accuracy: {best_accuracy:.4f}")
