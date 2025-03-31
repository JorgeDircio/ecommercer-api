from fastapi import APIRouter
from src.models.checkout import CartItem, PaymentData
from src.services.stripe_service import create_checkout_session, verify_session, payment_create

router = APIRouter()

@router.post("/stripe/create-checkout-session")
def create_session(data: list[CartItem]):
    session = create_checkout_session(data)
    return session


@router.post("/stripe/verify-session")
def create_session():
    session = verify_session()
    return session

@router.post("/stripe/payment-create")
def create_session(data: PaymentData):
    session = payment_create(data)
    return session
