import spacy
import os

nlp = spacy.load("en_core_web_sm", disable=["ner"])

def preprocess_text(text):

    sentences = text.split("\n")
    processed = []

    for doc in nlp.pipe(sentences, batch_size=32):

        tokens = [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct
        ]

        if len(tokens) > 5:
            processed.append(" ".join(tokens))

    return processed


def preprocess_folder():

    os.makedirs("data/processed", exist_ok=True)

    for file in os.listdir("data/raw"):

        with open(f"data/raw/{file}", encoding="utf-8") as f:
            text = f.read()

        sentences = preprocess_text(text)

        with open(f"data/processed/{file}", "w", encoding="utf-8") as f:
            f.write("\n".join(sentences))

    print("Prétraitement terminé")
