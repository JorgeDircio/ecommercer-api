from hashlib import sha256
import os
from dotenv import load_dotenv

load_dotenv()

def generate_sha256_hash(password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()