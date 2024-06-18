from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)

def test_get_all_services():
    response = client.get("/services")
    assert response.status_code == 200

def test_create_service():
    # Wrong number of parameters.
    response = client.post(
        "/services",
        json={}
    )
    assert response.status_code == 422

    # Wrong format.
    response = client.post(
        "/services",
        json={"name": 1,
              "duration_in_slots": 2}
    )
    assert response.status_code == 422

    # Ok.
    response = client.post(
        "/services",
        json={"name": "haircut",
              "duration_in_slots": 2}
    )
    assert response.status_code == 200

def test_get_service_by_id():
    # Get the last id.
    response = client.get("/services")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.get(f"services/{last_id + 1}")
    assert response.status_code == 404

    # Ok.
    response = client.get(f"/services/{last_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "haircut"
    assert response.json()["duration_in_slots"] == 2

def test_update_service_by_id():
    # Get the last id.
    response = client.get("/services")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.put(
        f"/services/{last_id + 1}",
        json={"name": "trim",
              "duration_in_slots": 1})
    assert response.status_code == 404

    # Ok.
    response = client.put(
        f"/services/{last_id}",
        json={"name": "trim",
              "duration_in_slots": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "trim"
    assert response.json()["duration_in_slots"] == 1

    # Revert.
    response = client.put(
        f"/services/{last_id}",
        json={"name": "haircut",
              "duration_in_slots": 2})
    assert response.status_code == 200

def test_delete_service_by_id():
    # Get the last id.
    response = client.get("/services")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.delete(f"/services/{last_id + 1}")
    assert response.status_code == 404

    # Ok.
    response = client.delete(f"/services/{last_id}")
    assert response.status_code == 200

    # Already deleted.
    response = client.delete(f"/services/{last_id}")
    assert response.status_code == 404
