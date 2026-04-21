from api.api_client import APIClient

def test_get_users():
    api = APIClient()
    response = api.get_users()
    assert response.status_code == 200

def test_create_user():
    api = APIClient()
    payload = {"name": "John", "job": "QA"}
    response = api.create_user(payload)
    assert response.status_code == 201
