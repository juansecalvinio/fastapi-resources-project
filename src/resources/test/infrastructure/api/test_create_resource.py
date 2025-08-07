from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_resources_and_returns_200():
  response = client.post("/resources/", json={ "url": "http://google.com" })
  assert response.status_code == 200
  assert response.json() == {"url": "http://google.com"}