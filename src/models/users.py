from pydantic import BaseModel

class User(BaseModel):
    id:int
    username:str
    fullname:str
    email:str
    disabled:bool

class UserDB(User):
    password:str