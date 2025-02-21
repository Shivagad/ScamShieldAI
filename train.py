import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset (ensure the file path is correct)
df = pd.read_csv("BETTER30.csv")

# Display first few rows (optional)
print("Raw Data:")
print(df.head())

# Define a helper function to convert labels to binary:
# Suspicious = 1, Not Suspicious = 0
def convert_label(label):
    return 1 if label.strip().lower() == "suspicious" else 0

# Apply conversion on the LABEL column if it's not null (ignore missing values)
df['LABEL'] = df['LABEL'].fillna("Not Suspicious")
df["binary_label"] = df["LABEL"].apply(convert_label)

# Aggregate conversation steps by concatenating all text entries per conversation
grouped = df.groupby("CONVERSATION_ID").agg({
    "TEXT": lambda texts: " ".join(texts),
    "binary_label": "max"  # If any step is suspicious, max() will be 1
}).reset_index()

# Rename for clarity
grouped.rename(columns={"TEXT": "conversation_text", "binary_label": "target"}, inplace=True)

print("\nAggregated Data:")
print(grouped.head())

# Features (X) and target labels (y)
X = grouped["conversation_text"]
y = grouped["target"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline: TF-IDF vectorization and Logistic Regression classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(solver="lbfgs", max_iter=1000))
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)

# Output performance metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Example of predicting a new call transcript
new_call = "Hello, this is David from the tax office. Your account has discrepancies. Please verify your bank details immediately to avoid legal consequences."
prediction = pipeline.predict([new_call])[0]
print("\nNew Call Prediction:", "Suspicious" if prediction == 1 else "Not Suspicious")
