import pytest

from api.user import user
from core.result_base import ResultBase

def test_add_user(login_user_1,get_user_1):
    cookies=login_user_1
    print(cookies)
    b=get_user_1
    payload = {
        "email": '834737865@qq.com',
        "permission_groups": ['7b447ab459aa11edb9e60242ac130014'],
        "realname":"wangliyan3",
        "remarks":"",
        "telephone":"18740084256",
        "username":"wangliyan6"
    }
    header = {
        "Content-Type": "application/JSON;charset=UTF-8",
        "Cookie":cookies
    }
    res = user.add_user(json=payload, headers=header)
    print(f"Response Status Code3: {res.status_code}")
    assert  res.status_code == 201

if __name__ == '__main__':
    pytest.main(["-q", "-s","test_01.py"])