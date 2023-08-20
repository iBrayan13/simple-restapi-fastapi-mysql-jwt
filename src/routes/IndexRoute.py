from fastapi import APIRouter, Depends
from src.models.users import User
from src.utils.security import Security

router = APIRouter()

@router.get("/")
async def index(regular_user:User = Depends(Security.verify_regular_user_jwt)):
    if not regular_user:
        return {
            'message' : 'Go to auth/signup to get register (send your information by a form) or auth/login for logging in (send your information by a form).'
                }
        
    print(Security.oauth2)
    return {'message' : f'Welcome {regular_user.username}. Go to user/me/read to get your information'}