from uuid import UUID
from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.models.request.payment import PaymentRequest
from src.databases.session_manager import get_session
from src.models.transaction.transaction import TransactionCreate
from src.services.transaction_service import create_transaction_service, list_transactions, get_transaction_by_id_service

router = APIRouter()


@router.post("/transactions")
async def create_transaction(
    data: PaymentRequest, session: Session = Depends(get_session)
):
    response = await create_transaction_service(session, data)
    return response


@router.get("/transactions")
def get_transactions(session: Session = Depends(get_session)):
    response = list_transactions(session)
    return response


@router.get("/transactions/{id}")
def get_transactions_by_id(id: UUID, session: Session = Depends(get_session)):
    response = get_transaction_by_id_service(id, session)
    return response
