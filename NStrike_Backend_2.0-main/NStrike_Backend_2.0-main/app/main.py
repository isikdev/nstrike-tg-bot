# app/main.py
from fastapi import FastAPI
from app.user.routes import router as user_router
from app.bet import routes as bet_routes
from app.transaction.routes import router as transaction_router
from app.event.routes import router as event_router
from app.role.routes import router as role_router
from app.admin.views import setup_admin
from app.database.db_init import async_engine, Base


app = FastAPI()

setup_admin(app)

@app.on_event("startup")
async def startup_event():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(bet_routes.router, prefix="/bets", tags=["bets"])
app.include_router(transaction_router, prefix="/transactions", tags=["transactions"])
app.include_router(event_router, prefix="/events", tags=["events"])
app.include_router(role_router, prefix="/roles", tags=["roles"])
@app.get("/")
def read_root():
    return {"message": "Welcome to the Betting App"}
