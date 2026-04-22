from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import rights, documents, health
import os

app = FastAPI(
    title="Cidadania AI API",
    description="AI-powered civic rights assistant API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(rights.router, prefix="/api/v1/rights", tags=["rights"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])


@app.get("/")
def root():
    return {"message": "Cidadania AI API is running", "version": "0.1.0"}
