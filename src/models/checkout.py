from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class ProductData(BaseModel):
    name: str


class Product(BaseModel):
    id: str
    product_data: ProductData
    unit_amount: float
    image: str
    currency: str


class CartItem(BaseModel):
    price_data: Product
    quantity: int


class CardInfo(BaseModel):
    number: str
    exp_month: int
    exp_year: int
    cvc: str
    name: str
    email: str
    amount: int


class PaymentData(BaseModel):
    amount: Decimal
    currency: str
    description: str | None
    metadata: Optional[dict] = None
    email_client: str | None
    confirm: bool | None
    card: Optional[CardInfo] = None
