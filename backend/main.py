# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.file_routes import router as file_router

app = FastAPI()

# Enable CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(file_router)

@app.get("/")
def read_root():
    return {"message": "Smart File QA Backend is Running"}
