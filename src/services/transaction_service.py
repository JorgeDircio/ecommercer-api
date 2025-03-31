from decimal import Decimal
from sqlmodel import Session, select
from src.models.request.payment import PaymentRequest
from src.databases.models.Transaction import Transaction, TransactionStatus
from src.models.transaction.transaction import TransactionCreate
from uuid import UUID
from typing import List, Optional
from src.services.blumon_pay_instance import blumon_client

async def create_transaction_service(session: Session, data: PaymentRequest) -> Transaction:
    try:
        payload = data.model_dump(mode='json')
        response = await blumon_client.post("ecommerce/charge", payload)

        blumon_transaction_id = response.get("id")
        status = TransactionStatus.completed if response.get("status") else TransactionStatus.failed
        
        transaction = Transaction(
            amount=Decimal(data.amount),
            currency=data.currency,
            customer_email=data.customerInformation.email,
            customer_name=f"{data.customerInformation.firstName} {data.customerInformation.middleName} {data.customerInformation.lastName}",
            status=status,
            blumonpay_transaction_id=blumon_transaction_id
        )
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return transaction.model_dump()
    except Exception as e:
        session.rollback()
        raise e


def get_transaction_by_id_service(id: UUID, session: Session) -> Optional[Transaction]:
    """Obtener una transacción por ID."""
    return session.get(Transaction, id)


def list_transactions(session: Session) -> List[Transaction]:
    """Listar todas las transacciones ordenadas por fecha descendente."""
    return session.exec(
        select(Transaction).order_by(Transaction.created_at.desc())
    ).all()
