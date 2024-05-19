from fastapi.testclient import TestClient

from ..main import app


client = TestClient(app)


def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200

def test_create_user():
    # Wrong number of parameters.
    response = client.post(
        "/users",
        json={"name": "test_user"}
    )
    assert response.status_code == 422

    # Wrong email format.
    response = client.post(
        "/users",
        json={"name": "test_user", "email": "test_email", "password": "test_password"}
    )
    assert response.status_code == 422

    # Ok.
    response = client.post(
        "/users",
        json={"name": "test_user", "email": "test@email.com", "password": "test_password"}
    )
    assert response.status_code == 200 or response.status_code == 400
    if response.status_code == 200:
        # Duplicate email.
        response = client.post(
            "/users",
            json={"name": "test_user", "email": "test@email.com", "password": "test_password"}
        )
        assert response.status_code == 400

def test_get_user_by_email():
    # Wrong email.
    response = client.get("/users/test_email")
    assert response.status_code == 404

    # Ok.
    response = client.get("/users/test@email.com")
    assert response.status_code == 200
    assert response.json()["name"] == "test_user"
    assert response.json()["password"] == "test_password"

def test_update_user_by_email():
    # Wrong email.
    response = client.put(
        "/users/test_email",
        json={"name": "test_user_updated", "password": "test_password_updated"})
    assert response.status_code == 404

    # Ok.
    response = client.put(
        "/users/test@email.com",
        json={"name": "test_user_updated", "password": "test_password_updated"})
    assert response.status_code == 200
    response = client.get("/users/test@email.com")
    assert response.status_code == 200
    assert response.json()["name"] == "test_user_updated"
    assert response.json()["password"] == "test_password_updated"

def test_delete_user_by_email():
    # Wrong email.
    response = client.delete("/users/test_email")
    assert response.status_code == 404

    # Ok.
    response = client.delete("/users/test@email.com")
    assert response.status_code == 200

    # Already deleted.
    response = client.delete("/users/test@email.com")
    assert response.status_code == 404
