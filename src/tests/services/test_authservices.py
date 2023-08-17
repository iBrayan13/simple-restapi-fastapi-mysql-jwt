from src.services.AuthServices import AuthService
from src.models.users import User, UserDB
from src.utils.security import Security
import pytest

@pytest.mark.parametrize("input_user",[
    UserDB(
        id=0, 
        username="test1",
        fullname="Test Tester",
        email="test1@test.com",
        disabled=False,
        password=Security.encrypt("test123")
    )
])
def test_signup_user(input_user:User):
    assert AuthService.register_user(input_user)

@pytest.mark.parametrize("input_user",[
    UserDB(
        id=0,
        username="test",
        fullname="Test Tester",
        email="test@test.com",
        disabled=False,
        password=Security.encrypt("test123")
    )
])
def test_false_signup_user(input_user:User):
    assert not AuthService.register_user(input_user)

@pytest.mark.parametrize("input_username, input_password",[("test", "test123")])
def test_login_user(input_username:str, input_password:str):
    authenticated_user = AuthService.login_user(input_username, Security.encrypt(input_password))
    assert type(authenticated_user) == User

@pytest.mark.parametrize("input_username, input_password",[("test2", "test123")])
def test_false_login_user(input_username:str, input_password:str):
    authenticated_user = AuthService.login_user(input_username, Security.encrypt(input_password))
    assert not type(authenticated_user) == User