# app/bet/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.bet.models import Bet
from app.bet.schemas import BetCreate, BetUpdate

async def get_bet_by_id(session: AsyncSession, bet_id: int):
    result = await session.execute(select(Bet).filter_by(id=bet_id))
    return result.scalars().first()

async def create_bet(session: AsyncSession, bet: BetCreate):
    new_bet = Bet(**bet.dict())
    session.add(new_bet)
    await session.commit()
    await session.refresh(new_bet)
    return new_bet

async def update_bet(session: AsyncSession, bet_id: int, bet: BetUpdate):
    existing_bet = await get_bet_by_id(session, bet_id)
    if existing_bet:
        for key, value in bet.dict().items():
            setattr(existing_bet, key, value)
        await session.commit()
        await session.refresh(existing_bet)
        return existing_bet
    return None

async def delete_bet(session: AsyncSession, bet_id: int):
    existing_bet = await get_bet_by_id(session, bet_id)
    if existing_bet:
        await session.delete(existing_bet)
        await session.commit()
        return True
    return False

async def get_all_bets(session: AsyncSession):
    result = await session.execute(select(Bet))
    return result.scalars().all()
