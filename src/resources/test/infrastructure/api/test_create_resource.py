from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_resources_and_returns_201():
  response = client.post("/resources/", data={
    "url": "http://google.com"
  })
  assert response.status_code == 201
  assert response.json() == {"url": "http://google.com"}