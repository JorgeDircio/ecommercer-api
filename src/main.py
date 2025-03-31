import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.routers.auth import router as stripe_router
from src.routers.transaction import router as transaction_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Payments API")

base_url_front = os.getenv("BASE_URL_FRONT")
api_base = os.getenv("API_BASE")

if not base_url_front or not api_base:
    raise HTTPException(status_code=500, detail="Environment variables not configured.")

origins = [base_url_front]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    allow_methods=["POST", "GET", "PUT", "DELETE"],
)
app.include_router(stripe_router, prefix=f"{os.getenv('API_BASE')}")
app.include_router(transaction_router, prefix=f"{os.getenv('API_BASE')}")
