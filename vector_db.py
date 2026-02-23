import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import streamlit as st

@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_embedder()
index = faiss.IndexFlatL2(384)
texts = []

def add_to_vector_db(text):
    emb = model.encode([text]).astype("float32")
    index.add(emb)
    texts.append(text)

def search_vector_db(query, k=1):
    emb = model.encode([query]).astype("float32")
    _, I = index.search(emb, k)

    results = []
    for i in I[0]:
        if i < len(texts):
            topic = texts[i].split("\n")[0]   # Take first line
            results.append(topic)
    
    return results