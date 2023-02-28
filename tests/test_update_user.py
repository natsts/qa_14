import requests
from pytest_voluptuous import S
from schemas.user import update_user


def test_update_user():
    response = requests.patch(url='https://reqres.in/api/users/2', json={"name": "morpheus", "job": "zion resident"})

    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()['job'] == "zion resident"
