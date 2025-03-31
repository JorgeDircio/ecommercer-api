from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional
from datetime import datetime


class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=5, example="mxn")
    customer_email: EmailStr = Field(example="example@correo.com")
    customer_name: str = Field(example="Juan Pérez")

class TransactionStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class TransactionRead(TransactionCreate):
    id: UUID
    status: TransactionStatus
    blumonpay_transaction_id: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
