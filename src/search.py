import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from src.embedder.py import model

index = faiss.read_index("models/semantic.index")

with open("embeddings/sentences.pkl", "rb") as f:
    sentences = pickle.load(f)


def search(query, k=5):

    q_emb = model.encode([query]).astype("float32")

    distances, indices = index.search(q_emb, k)

    return [sentences[i] for i in indices[0]]
