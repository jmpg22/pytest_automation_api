import pytest
import uuid
from utils.api_client import APIClient

@pytest.fixture(scope='module')
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client, load_user_data):
    user_data = load_user_data["new_user"]  # Fix: Use dictionary access instead of function call
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    response = api_client.post('users', user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['username'] == "obaidsqa"
    assert len(response.json()) > 0
    
    #id = response.json()['id']
    
    response = api_client.get('users/10')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()['name'] == 'Clementina DuBuque'
    assert response.json()['username'] == 'Moriah.Stanton'
    assert response.json()['email'] == 'Rey.Padberg@karina.biz'

def test_update_users(api_client):
    user_data = {
        'name': 'Obaid',
        'username': 'obaidsqa',
        'email': 'test@gmail.com'
    }
    response = api_client.put('users/10', user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['username'] == "obaidsqa"
    assert len(response.json()) > 0

def test_delete_users(api_client):
    response = api_client.delete('users/10')
    print(response.json())
    assert response.status_code == 200