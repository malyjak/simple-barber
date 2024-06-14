from datetime import date, timedelta

from fastapi.testclient import TestClient
from ..main import app


client = TestClient(app)
today = date.today()
tomorrow = today + timedelta(days=1)

def test_get_all_slots():
    response = client.get("/admin/slots")
    assert response.status_code == 200

def test_create_slot():
    # Wrong number of parameters.
    response = client.post(
        "/admin/slots",
        json={}
    )
    assert response.status_code == 422

    # Wrong date format.
    response = client.post(
        "/admin/slots",
        json={"date": "2014-01"}
    )
    assert response.status_code == 422

    # Ok.
    response = client.post(
        "/admin/slots",
        json={"date": str(today)}
    )
    assert response.status_code == 200

def test_get_slot_by_id():
    # Get the last id.
    response = client.get("/admin/slots")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.get(f"/admin/slots/{last_id + 1}")
    assert response.status_code == 404

    # Ok.
    response = client.get(f"/admin/slots/{last_id}")
    assert response.status_code == 200
    assert response.json()["date"] == str(today)
    assert response.json()["occupied"] == False

def test_update_slot_by_id():
    # Get the last id.
    response = client.get("/admin/slots")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.put(
        f"/admin/slots/{last_id + 1}",
        json={"date": str(tomorrow),
              "occupied": True})
    assert response.status_code == 404

    # Ok.
    response = client.put(
        f"/admin/slots/{last_id}",
        json={"date": str(tomorrow),
              "occupied": True})
    assert response.status_code == 200
    assert response.json()["date"] == str(tomorrow)
    assert response.json()["occupied"] == True

    # Revert.
    response = client.put(
        f"/admin/slots/{last_id}",
        json={"date": str(today),
              "occupied": False})
    assert response.status_code == 200

def test_delete_slot_by_id():
    # Get the last id.
    response = client.get("/admin/slots")
    last_id = response.json()[-1]["id"]

    # Wrong id.
    response = client.delete(f"/admin/slots/{last_id + 1}")
    assert response.status_code == 404

    # Ok.
    response = client.delete(f"/admin/slots/{last_id}")
    assert response.status_code == 200

    # Already deleted.
    response = client.delete(f"/admin/slots/{last_id}")
    assert response.status_code == 404
