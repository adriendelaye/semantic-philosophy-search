# Semantic Philosophy Search

A semantic search engine for philosophical texts using modern NLP techniques (Sentence Transformers + FAISS).

This project scrapes philosophical content, processes it, encodes it into embeddings, and allows users to query it through a fast semantic search interface.

Tips and advices are welcomed.

---

## Features

* Semantic search (not keyword-based)
* Sentence embeddings with SentenceTransformers
* Fast vector search using FAISS
* Web scraping from Stanford Encyclopedia of Philosophy
* Interactive UI with Streamlit
* End-to-end NLP pipeline

---

## Project Structure

```
semantic-search/
│
├── data/
│   ├── raw/              # Raw scraped texts
│   └── processed/        # Cleaned & segmented texts
│
├── models/
│   ├── embeddings.npy    # Sentence embeddings
│   ├── sentences.pkl     # Corresponding text chunks
│   └── faiss_index.bin   # FAISS index
│
├── src/
│   ├── scraper.py
│   ├── preprocess.py
│   ├── build_embeddings.py
│   ├── build_index.py
│   └── search.py
│
├── app.py
├── build_pipeline.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/adriendelaye/semantic-philosophy-search.git
cd semantic-philosophy-search
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Build the Pipeline

Run the full NLP pipeline:

```
python build_pipeline.py
```

This will:

1. Scrape philosophical texts
2. Clean and preprocess them
3. Generate sentence embeddings
4. Build a FAISS index

Expected outputs:

```
data/raw/
data/processed/
models/embeddings.npy
models/sentences.pkl
models/faiss_index.bin
```

---

## Run the App

```
python -m streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

## Important Notes

* You must run the pipeline before launching the app
* Large downloads may occur when loading models
* First run may take a few minutes

---

## Tech Stack

* Python
* SentenceTransformers
* FAISS
* BeautifulSoup
* Streamlit
* NumPy / Scikit-learn

---

## Future Improvements

* Retrieval-Augmented Generation (RAG)
* Relevance scoring
* Multi-language support
* Linguistic feature filtering (POS, syntax)

---

## Author

Adrien Delaye

---

## Why this project?

This project demonstrates:

* Applied NLP skills
* End-to-end ML pipeline design
* Semantic search implementation
* Real-world data handling

---
