from fastapi import FastAPI
from src.routes import UserRoutes, AuthRoutes

app = FastAPI()

#routes
app.include_router(router=UserRoutes.router, prefix="/user")
app.include_router(router=AuthRoutes.router, prefix="/auth")