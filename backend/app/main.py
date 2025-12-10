from fastapi import FastAPI
import pandas as pd
from features import compute_features

app = FastAPI()

# Load sample data
df = pd.read_csv("app/sample_data.csv")
df_features = compute_features(df)

@app.get("/")
def read_root():
    return {"message": "CourtMomentum backend running!"}

@app.get("/features")
def get_features():
    # Return computed features as JSON
    return df_features.to_dict(orient="records")
