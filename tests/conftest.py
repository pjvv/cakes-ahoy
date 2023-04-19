import moto
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)

    yield client


@pytest.fixture(autouse=True)
def dynamodb_mock():
    with moto.mock_dynamodb():
        yield
