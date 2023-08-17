from decouple import config
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.models.users import User
from src.services.UserServices import UserService
import hashlib


class Security:
    oauth2 = OAuth2PasswordBearer(tokenUrl="token")
    TOKEN_KEY = config("JWT_KEY")
    TOKEN_ALGORITHM = config("JWT_ALGORITHM")
    TOKEN_DURATION = int(config("JWT_TOKEN_DURATION"))

    @classmethod
    def create_user_jwt(cls, user:User) -> str:
        """Get a new token with a duration of two minutes.

        Args:
            user (User): user who is creating a token.

        Returns:
            str: json web token.
        """
        try:
            duration = datetime.utcnow() + timedelta(minutes=cls.TOKEN_DURATION)
            
            payload = {
                "sub":user.username,
                "fullname":user.fullname,
                "disabled":user.disabled,
                "exp":duration
            }

            return jwt.encode(claims=payload, key=cls.TOKEN_KEY, algorithm=cls.TOKEN_ALGORITHM)
        except Exception as e:
            print(e)
            return None
    
    @classmethod
    def verify_regular_user_jwt(cls, token_to_verify:str = Depends(oauth2)) -> User:
        """Verify if the user has access to the regular services.

        Args:
            token_to_verify (str, optional): dependency to get the bearer token. Defaults to Depends(oauth2).

        Returns:
            User: autherizated user.
        """
        try:
            payload = jwt.decode(token=token_to_verify, key=cls.TOKEN_KEY, algorithms=[cls.TOKEN_ALGORITHM])
            if not len(payload["sub"]) > 0 and len(payload["fullname"]) > 0 and payload["disabled"] == bool:
                return None
            return UserService.read_user_by_username(payload["sub"])
        except Exception as e:
            print(e)
            return None

    
    @classmethod
    def verify_admin_user_jwt(cls, token_to_verify:str = Depends(oauth2)) -> User:
        """Verify if the user has access to the admin services.

        Args:
            token_to_verify (str, optional): dependency to get the bearer token. Defaults to Depends(oauth2).

        Returns:
            User: autherizated user.
        """
        try:
            payload = jwt.decode(token=token_to_verify, key=cls.TOKEN_KEY, algorithms=[cls.TOKEN_ALGORITHM])
            if not payload["disabled"]:
                return None
            
            return UserService.read_user_by_username(payload["sub"])
        except Exception as e:
            print(e)
            return None
    
    @classmethod
    def encrypt(cls, text:str) -> str:
        """Become a normal text to a encrypted text

        Args:
            text (str): text to encrypt.

        Returns:
            str: encrypted text.
        """
        new_text = text.encode("utf-8")
        hashed = hashlib.sha256(new_text)
        return hashed.hexdigest()