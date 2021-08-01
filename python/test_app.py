from app import app

client = app.test_client()

def test_hello():
    response = client.get("/")
    assert response.status_code == 200