# ml_model.py
import pickle
import os

# Load model and vectorizer when module is imported
MODEL_PATH = "model.pkl"
VEC_PATH = "vectorizer.pkl"

ml_available = False

if os.path.exists(MODEL_PATH) and os.path.exists(VEC_PATH):
    try:
        model = pickle.load(open(MODEL_PATH, "rb"))
        vectorizer = pickle.load(open(VEC_PATH, "rb"))
        ml_available = True
    except:
        ml_available = False


def predict_spam(text: str) -> bool:
    """
    Returns True = Spam, False = Not Spam
    """
    if not ml_available:
        # Fail-safe: if ML files missing, always return False
        return False

    x = vectorizer.transform([text])
    pred = model.predict(x)[0]
    return bool(pred)