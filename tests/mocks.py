from typing import Any


def get_mock_create_request() -> dict[str, Any]:
    return {
        "comment": "abc",
        "id": 123,
        "imageUrl": "http://example.com",
        "name": "best",
        "yumFactor": 1,
    }
