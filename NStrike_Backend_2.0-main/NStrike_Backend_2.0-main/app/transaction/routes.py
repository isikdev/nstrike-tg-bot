# app/transaction/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db_init import get_session
from app.transaction import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Transaction)
async def create_transaction(transaction: schemas.TransactionCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_transaction(db, transaction)

@router.get("/{transaction_id}", response_model=schemas.Transaction)
async def read_transaction(transaction_id: int, db: AsyncSession = Depends(get_session)):
    db_transaction = await crud.get_transaction(db, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.put("/{transaction_id}", response_model=schemas.Transaction)
async def update_transaction(transaction_id: int, transaction: schemas.TransactionUpdate, db: AsyncSession = Depends(get_session)):
    db_transaction = await crud.update_transaction(db, transaction_id, transaction)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.delete("/{transaction_id}", response_model=schemas.Transaction)
async def delete_transaction(transaction_id: int, db: AsyncSession = Depends(get_session)):
    success = await crud.delete_transaction(db, transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted"}

@router.get("/", response_model=list[schemas.Transaction])
async def read_transactions(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    transactions = await crud.get_transactions(db, skip=skip, limit=limit)
    return transactions
