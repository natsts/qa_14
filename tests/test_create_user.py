import requests
from pytest_voluptuous import S
from schemas.user import new_user_schema


def test_create_user():
    response = requests.post(url='https://reqres.in/api/users', json={'name': 'morpheus', 'job': 'leader'})

    assert response.status_code == 201
    assert S(new_user_schema) == response.json()
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'
