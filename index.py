from fastapi import FastAPI
from src.routes import IndexRoute, UserRoutes, AuthRoutes

app = FastAPI()

#routes
app.include_router(router=IndexRoute.router, prefix="", tags=["Index"])
app.include_router(router=UserRoutes.router, prefix="/user", tags=["User"])
app.include_router(router=AuthRoutes.router, prefix="/auth", tags=["Auth"])