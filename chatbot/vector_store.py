import numpy as np

store = {
    "chunks": [],
    "vectors": None
}

def build_store(chunks, vectors):
    store["chunks"] = chunks
    store["vectors"] = np.array(vectors)

def cosine_similarity(a, b):
    a = a.flatten()
    dot_product = np.dot(b, a)
    norms = np.linalg.norm(b, axis=1) * np.linalg.norm(a)
    return dot_product / norms

def search(query_vector, top_k=5):
    scores = cosine_similarity(query_vector, store["vectors"])
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for i in top_indices:
        results.append({
            "text":          store["chunks"][i]["text"],
            "product_id":    store["chunks"][i]["product_id"],
            "product_title": store["chunks"][i]["product_title"],
            "score":         round(float(scores[i]), 4)
        })
    return results
