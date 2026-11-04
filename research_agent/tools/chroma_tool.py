import chromadb
from sentence_transformers import SentenceTransformer
_model = SentenceTransformer("all-MiniLM-L6-v2")
_client = chromadb.PersistentClient(path="./chroma_db")
def get_collection(name="research"): return _client.get_or_create_collection(name, metadata={"hnsw:space": "cosine"})
def add_chunks(collection, chunks: list[dict]):
    if not chunks: return
    texts = [c["text"] for c in chunks]
    collection.add(ids=[c["id"] for c in chunks], documents=texts, embeddings=_model.encode(texts).tolist(), metadatas=[{"url": c["url"], "title": c["title"]} for c in chunks])
def query(collection, text: str, k: int = 8): return collection.query(query_embeddings=_model.encode([text]).tolist(), n_results=k)