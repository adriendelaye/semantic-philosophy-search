from src.scraper import scrape
from src.preprocess import preprocess_folder
from src.embedder import build_embeddings
from src.indexer import build_index

topics = ["meaning", "reference", "semantics", "speech-acts"]

if __name__ == "__main__":
  scrape(topics)
  preprocess_folder()
  build_embeddings()
  build_index()

  print("Pipeline terminé")
