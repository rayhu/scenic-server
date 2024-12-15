from fastapi.testclient import TestClient
from src.app.main import app

# Create a TestClient instance
client = TestClient(app)


def test_read_root():
    # Send a GET request to the root endpoint
    response = client.get("/")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected output
    assert response.json() == {"Hello": "Scenic Server"}
