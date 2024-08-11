# app/transaction/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.transaction.models import Transaction
from app.transaction.schemas import TransactionCreate, TransactionUpdate

async def get_transaction(db: AsyncSession, transaction_id: int):
    result = await db.execute(select(Transaction).filter(Transaction.id == transaction_id))
    return result.scalars().first()

async def create_transaction(db: AsyncSession, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction

async def update_transaction(db: AsyncSession, transaction_id: int, transaction: TransactionUpdate):
    db_transaction = await get_transaction(db, transaction_id)
    if db_transaction:
        for key, value in transaction.dict().items():
            setattr(db_transaction, key, value)
        await db.commit()
        await db.refresh(db_transaction)
        return db_transaction
    return None

async def delete_transaction(db: AsyncSession, transaction_id: int):
    db_transaction = await get_transaction(db, transaction_id)
    if db_transaction:
        await db.delete(db_transaction)
        await db.commit()
        return True
    return False

async def get_transactions(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Transaction).offset(skip).limit(limit))
    return result.scalars().all()
