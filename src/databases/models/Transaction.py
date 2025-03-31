from sqlmodel import SQLModel, Field
from enum import StrEnum
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime


class TransactionStatus(StrEnum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class Transaction(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=5)
    customer_email: str = Field(default=None)
    customer_name: str = Field(default=None)
    status: TransactionStatus = Field(default="pending")
    blumonpay_transaction_id: Optional[str] = Field(default=None, index=True)
    created_at: datetime = Field(default_factory=datetime.now)