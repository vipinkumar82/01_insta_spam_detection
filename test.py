# test.py - Train an Instagram spam prediction ML model

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# -------------------------------
#  TRAINING DATASET
# -------------------------------
data = {
    "text": [
        "Buy now and get 50% discount",
        "Click here to win money",
        "Free followers instantly",
        "DM me for free crypto profit",
        "Limited time offer",
        "Win lottery now",
        "Get rich quick with bitcoin",
        "Follow me for big money",
        "This is a completely normal post",
        "Beautiful picture brother",
        "Amazing sunset view",
        "I love this photo!",
        "Nice shot bro!",
        "Wow amazing picture",
        "Happy birthday!"
    ],
    "label": [
        1, 1, 1, 1,
        1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0
    ]
}

df = pd.DataFrame(data)

# -------------------------------
#  TF-IDF VECTORIZER
# -------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# -------------------------------
#  ML MODEL
# -------------------------------
model = LogisticRegression(max_iter=1500)
model.fit(X, y)

# -------------------------------
#  SAVE MODEL + VECTORIZER
# -------------------------------
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ ML Model trained and saved as model.pkl + vectorizer.pkl")