import requests
from pytest_voluptuous import S
from schemas.user import single_user_schema


def test_get_users():
    response = requests.get(url='https://reqres.in/api/users', params={'id': 2})

    assert response.status_code == 200
    assert S(single_user_schema) == response.json()
    assert response.json()['data']['id'] == 2
