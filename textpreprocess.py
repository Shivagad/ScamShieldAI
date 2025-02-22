import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# ========== LOAD DATA ==========
# Replace 'your_file.csv' with the actual file path
df = pd.read_csv("cleaned_dataset.csv")

# ========== TEXT PREPROCESSING FUNCTION ==========
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Handle negations (e.g., "isn't" → "is not")
    negations = {"aren't": "are not", "isn't": "is not", "don't": "do not", "didn't": "did not", "won't": "will not",
                 "can't": "can not", "wasn't": "was not", "shouldn't": "should not", "couldn't": "could not",
                 "haven't": "have not", "hasn't": "has not", "weren't": "were not", "wouldn't": "would not"}
    for neg, expanded in negations.items():
        text = text.replace(neg, expanded)

    # Remove special characters, numbers, and extra spaces
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords (except "not" to retain negation meaning)
    stop_words = set(stopwords.words('english')) - {"not"}
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Apply preprocessing
df["cleaned_text"] = df["text"].apply(preprocess_text)

# Save cleaned data (optional)
df.to_csv("cleaned_data.csv", index=False)

# Print first few rows
print(df.head())
