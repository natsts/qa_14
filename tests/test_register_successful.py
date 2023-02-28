import requests
from pytest_voluptuous import S
from schemas.user import successful_register_user


def test_register_successful():
    response = requests.post(url='https://reqres.in/api/register', json={"email": "eve.holt@reqres.in", "password": "pistol"})

    assert response.status_code == 200
    assert S(successful_register_user) == response.json()
    assert response.json()['id'] == 4
