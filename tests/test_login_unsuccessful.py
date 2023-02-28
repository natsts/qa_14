import requests
from pytest_voluptuous import S
from schemas.user import login_unsuccessful_user


def test_login_unsuccessful():
    response = requests.post(url='https://reqres.in/api/login', json={"email": "peter@klaven"})

    assert response.status_code == 400
    assert S(login_unsuccessful_user) == response.json()
