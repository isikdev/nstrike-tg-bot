# app/admin/views.py
from sqladmin import Admin, ModelView
from app.user.models import User
from app.bet.models import Bet
from app.event.models import Event
from app.role.models import Role
from app.transaction.models import Transaction
from app.database.db_init import async_engine
from app.admin.admin_auth import BasicAuthBackend
from fastapi import FastAPI

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.first_name, User.last_name, User.username, User.balance, User.usdt_balance, User.ammo]

class BetAdmin(ModelView, model=Bet):
    column_list = [Bet.id, Bet.user_id, Bet.amount, Bet.odds, Bet.result, Bet.placed_at]

class EventAdmin(ModelView, model=Event):
    column_list = [Event.id, Event.name, Event.start_time, Event.end_time, Event.description]

class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name, Role.description]

class TransactionAdmin(ModelView, model=Transaction):
    column_list = [Transaction.id, Transaction.user_id, Transaction.amount, Transaction.timestamp]

def setup_admin(app: FastAPI):
    admin = Admin(app, async_engine, authentication_backend=BasicAuthBackend())
    admin.add_view(UserAdmin)
    admin.add_view(BetAdmin)
    admin.add_view(EventAdmin)
    admin.add_view(RoleAdmin)
    admin.add_view(TransactionAdmin)
