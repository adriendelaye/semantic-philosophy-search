from sentence_transformers import SentenceTransformer
import os
import pickle
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

def build_embeddings():

    model = SentenceTransformer(MODEL_NAME)

    sentences = []

    for file in os.listdir("data/processed"):
        with open(f"data/processed/{file}", encoding="utf-8") as f:
            sentences += f.read().split("\n")

    embeddings = model.encode(sentences, show_progress_bar=True)

    np.save("models/embeddings.npy", embeddings)

    with open("models/sentences.pkl", "wb") as f:
        pickle.dump(sentences, f)

    print(f"{len(sentences)} phrases encodées")
