from fastapi import HTTPException, status
from models.cake import CakeApi as ApiCake
from pynamodb import exceptions

from persistence.models import CakeDb


def get_all_cakes() -> list[ApiCake]:
    """Retrieve all the cakes from DynamoDB.

    NOTE: this is limited to 10 currently.

    Returns:
        list[ApiCake]: a list of cakes
    """
    cakes_db = CakeDb.scan(limit=10)  # limiting this to prevent huge scans

    cakes = []
    for cake in cakes_db:
        cakes.append(cake.attribute_values)

    return cakes


def add_cake(api_model: ApiCake):
    """Add a cake to the DynamoDB table.

    Args:
        api_model (ApiCake): the cake to be added

    Raises:
        HTTPException: returns HTTP 500 if the record is not saved
    """
    try:
        CakeDb(**api_model.dict()).save()
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cake not saved due to internal error",
        ) from exc


def delete_cake(cake_id: int):
    """Delete a Cake within DynamoDB using the supplied identifier.

    Args:
        cake_id (int): identifier of the cake

    Raises:
        HTTPException: returns HTTP 404 if attempting to delete a cake which is not present
        HTTPException: returns HTTP 500 if an unexpected error occurred
    """
    try:
        CakeDb.get(cake_id).delete()
    except (exceptions.GetError, exceptions.DoesNotExist) as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cake not found",
        ) from exc
    except exceptions.DeleteError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cake not deleted due to internal error",
        ) from exc
