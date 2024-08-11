# app/bet/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db_init import get_session
from app.bet import crud
from app.bet.schemas import BetCreate, BetUpdate

router = APIRouter()

@router.post("/bets/")
async def create_bet(bet: BetCreate, session: AsyncSession = Depends(get_session)):
    return await crud.create_bet(session, bet)

@router.get("/bets/{bet_id}")
async def read_bet(bet_id: int, session: AsyncSession = Depends(get_session)):
    bet = await crud.get_bet_by_id(session, bet_id)
    if bet is None:
        raise HTTPException(status_code=404, detail="Bet not found")
    return bet

@router.put("/bets/{bet_id}")
async def update_bet(bet_id: int, bet: BetUpdate, session: AsyncSession = Depends(get_session)):
    updated_bet = await crud.update_bet(session, bet_id, bet)
    if updated_bet is None:
        raise HTTPException(status_code=404, detail="Bet not found")
    return updated_bet

@router.delete("/bets/{bet_id}")
async def delete_bet(bet_id: int, session: AsyncSession = Depends(get_session)):
    success = await crud.delete_bet(session, bet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bet not found")
    return {"message": "Bet deleted"}

@router.get("/bets/")
async def read_all_bets(session: AsyncSession = Depends(get_session)):
    bets = await crud.get_all_bets(session)
    return bets
