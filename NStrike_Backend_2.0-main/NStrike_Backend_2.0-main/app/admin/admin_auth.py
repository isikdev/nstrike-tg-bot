# app/admin/admin_auth.py
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser, UnauthenticatedUser

security = HTTPBasic()

class BasicAuthBackend(AuthenticationBackend):
    def __init__(self):
        self.username = "admin"
        self.password = "password"

    async def authenticate(self, request):
        credentials = await security(request)
        if credentials.username == self.username and credentials.password == self.password:
            return AuthCredentials(["authenticated"]), SimpleUser(self.username)
        return AuthCredentials([]), UnauthenticatedUser()
