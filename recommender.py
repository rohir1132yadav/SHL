import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load pre-trained transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load SHL assessment catalog
df = pd.read_csv('shl_catalog.csv')
df["embedding"] = df["name"].apply(lambda x: model.encode(x, convert_to_tensor=True))

def recommend_assessments(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    df["score"] = df["embedding"].apply(lambda x: util.pytorch_cos_sim(query_embedding, x).item())
    
    results = df.sort_values(by="score", ascending=False).head(10)[["name", "url", "remote", "adaptive", "duration", "type"]]
    return results.to_dict(orient='records')
