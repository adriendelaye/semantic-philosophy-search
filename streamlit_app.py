import os
import streamlit as st
from src.search import search
from build_pipeline import build_pipeline

if not os.path.exists("models/faiss_index.bin"):
    st.error("Please run build_pipeline.py first")
    st.stop()
    
st.set_page_config(page_title="Semantic Philosophy Search", layout="centered")

st.title("Semantic Philosophy Search")

st.write("Ask any question about philosophy and get somewhat relevant answers.")

query = st.text_input("Your question:")

if query:

    results = search(query, k=3)

    st.subheader("Top results:")

    for i, res in enumerate(results, 1):
        st.write(f"**{i}.** {res}")
