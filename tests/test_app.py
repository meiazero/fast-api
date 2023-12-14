from fastapi.testclient import TestClient


def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olai mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'password': 'secret',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
    }


def test_read_users(client: TestClient):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'test',
                'email': 'test@test.com',
            },
        ],
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test',
            'email': 'test@test.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
