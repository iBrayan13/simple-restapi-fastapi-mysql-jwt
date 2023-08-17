from fastapi import APIRouter, HTTPException, status, Depends
from src.models.users import User, UserDB
from src.services.UserServices import UserService
from src.utils.security import Security

router = APIRouter()

token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Credentials invalid.",
    headers={"WWW-Authenticated":"Bearer"}
    )

#Regular routes
@router.get("/me/read")
async def me(regular_user:User = Depends(Security.verify_regular_user_jwt)):
    if not regular_user:
        raise token_exception
    
    return {regular_user.username:regular_user}

#Admin routes
@router.get("/read/all")
async def read_all_users(admin_user:User = Depends(Security.verify_admin_user_jwt)):
    if not admin_user:
        raise token_exception
    
    users = UserService.read_users()
    if not len(users) > 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="There's no any user in database.")
    
    return users

@router.put("/update")
async def update_user(user:User, admin_user:User = Depends(Security.verify_admin_user_jwt)):
    if not admin_user:
        raise token_exception
    
    updated = UserService.update_user(user)
    if not updated:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="User data invalid.")
    
    return {"success":True}

@router.delete("/delete/{id}")
async def delete_user(id:int, admin_user:User = Depends(Security.verify_admin_user_jwt)):
    if not admin_user:
        raise token_exception
    
    deleted = UserService.delete_user(id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="User data invalid.")
    
    return {"success":True}