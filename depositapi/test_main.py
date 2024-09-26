from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_calculating():
    response = client.post('/calculate', json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    })
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert "31.01.2021" in response.json().keys()
    assert "28.02.2021" in response.json().keys()
    assert "31.03.2021" in response.json().keys()


def test_invalid_date():
    response = client.post("/calculate", json={
        "date": "31-01-2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6.5
    })
    assert response.status_code == 400