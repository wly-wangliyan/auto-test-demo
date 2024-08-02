import pytest

from api.user import user
from common.logger import logger
from core.result_base import ResultBase

@pytest.fixture(scope="session")
def login_user_1():
    payload = {
        "username": '88888888',
        "password": 'admin_123'
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, headers=header)
    print(f"Response Status Code0: {res.status_code}")
    aa=res.headers.get('Set-Cookie')
    print(f"Response cookie: {aa}")
    return aa

@pytest.fixture(scope="session")
def get_user_1(login_user_1):
    cookies=login_user_1
    print(cookies)
    cookie = {"Cookie":cookies}
    res = user.get_user(headers=cookie)
    print(f"Response Status Code1: {res.status_code}")
    return res.status_code