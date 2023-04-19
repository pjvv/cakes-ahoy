from fastapi import status
from fastapi.testclient import TestClient
from models.cake import CakeApi
from persistence.models import CakeDb, ensure_table_is_created

from tests.mocks import get_mock_create_request


def create_cake():
    cake = CakeDb(**CakeApi.parse_obj(get_mock_create_request()).dict())
    cake.save()

    return cake


def test_get_cakes(test_client: TestClient):
    ensure_table_is_created()
    cake = create_cake()
    assert CakeDb().count() == 1

    response = test_client.get(f"/v1/cakes")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0] == cake.attribute_values

    cake.delete()
    response = test_client.get(f"/v1/cakes")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_add_cake(test_client: TestClient):
    ensure_table_is_created()

    response = test_client.post("/v1/cakes", json=get_mock_create_request())

    assert CakeDb.count() == 1
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == get_mock_create_request()


def test_remove_cake(test_client: TestClient):
    ensure_table_is_created()

    response = test_client.delete("/v1/cakes/123")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    create_cake()
    assert CakeDb.count() == 1

    response = test_client.delete("/v1/cakes/123")
    assert response.status_code == status.HTTP_200_OK
