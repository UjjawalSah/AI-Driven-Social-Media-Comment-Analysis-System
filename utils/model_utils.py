import pickle
from pathlib import Path
from utils.preprocess import clean_text


def load_model_vectorizer():
    model_path = Path("models/cyberbullying_model_model.pkl")
    vectorizer_path = Path("models/cyberbullying_vectorizer.pkl")

    if model_path.exists() and vectorizer_path.exists():
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        with open(vectorizer_path, 'rb') as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)
        return model, vectorizer
    else:
        raise FileNotFoundError("Model or vectorizer file not found!")

def predict_cyberbullying(texts, vectorizer, model):
    cleaned_texts = [clean_text(text) for text in texts]
    tfidf_matrix = vectorizer.transform(cleaned_texts)
    return model.predict(tfidf_matrix)
