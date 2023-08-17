from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from src.services.AuthServices import AuthService
from src.utils.security import Security
from src.models.users import UserDB

router = APIRouter()

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(form:OAuth2PasswordRequestForm = Depends()):
    username = form.username
    password = form.password
    user = AuthService.login_user(username, Security.encrypt(password))
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user data.")

    access_token = Security.create_user_jwt(user)
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something was wrong while creating the bearer token."
            )
    
    return {"access_token":access_token, "type_token":"bearer"}

@router.post("/signup")
async def register(
    username:str = Form(),
    fullname:str = Form(),
    email:str = Form(),
    disabled:bool = Form(),
    password:str = Form()
    ):
    user = UserDB(
        id=0, 
        username=username,
        fullname=fullname,
        email=email,
        disabled=disabled,
        password=Security.encrypt(password)
        )
    register = AuthService.register_user(user)
    if not register:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user data.")
    
    return RedirectResponse("/auth/login")