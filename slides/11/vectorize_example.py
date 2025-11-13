from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
text = "Мама мыла раму"
emb = model.encode(text, normalize_embeddings=True)

print(emb[:8])     # первые числа векторa

# emb.ndim        # число измерений (1 или 2)
# emb.shape[0]    # длина вектора, или размер батча
# emb.shape[-1]   # размер эмбеддинга (например, 384)
# len(emb)        # то же, что emb.shape[0] для 1D