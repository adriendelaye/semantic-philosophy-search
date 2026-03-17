import faiss
import numpy as np
import os

def build_index():

    embeddings = np.load("models/embeddings.npy")

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(embeddings)

    os.makedirs("models", exist_ok=True)
    faiss.write_index(index, "models/faiss_index.bin")

    print(f"Index FAISS créé avec {index.ntotal} vecteurs")
