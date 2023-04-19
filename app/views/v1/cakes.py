import persistence.crud as crud
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models import responses
from models.cake import CakeApi

router = APIRouter()


@router.get(
    "/v1/cakes",
    name="List cakes",
    description="List all the available cakes.",
    responses={
        200: {"model": list[CakeApi]},
        400: {"model": responses.BadRequestResponse},
        500: {"model": responses.InternalErrorResponse},
    },
)
def list_cakes() -> JSONResponse:
    """List all the available cakes.

    Returns:
        JSONResponse: A JSON response containing a list with cake objects.
    """
    cakes = crud.get_all_cakes()

    return JSONResponse(content=cakes)


@router.post(
    "/v1/cakes",
    name="Add cake",
    description="Add a cake.",
    responses={
        201: {"model": CakeApi},
        400: {"model": responses.BadRequestResponse},
        500: {"model": responses.InternalErrorResponse},
    },
)
def add_cake(cake: CakeApi) -> JSONResponse:
    """Add a cake to the collection.

    Args:
        cake (Cake): the cake to be added

    Returns:
        JSONResponse: Returns a JSON representation of the cake which was saved.
    """
    crud.add_cake(cake)

    return JSONResponse(content=cake.dict(by_alias=True), status_code=status.HTTP_201_CREATED)


@router.delete(
    "/v1/cakes/{cake_id}",
    name="Remove cake",
    description="Remove a cake.",
    responses={
        200: {},
        400: {"model": responses.BadRequestResponse},
        500: {"model": responses.InternalErrorResponse},
    },
)
def delete_cake(cake_id: int) -> JSONResponse:
    """Remove a cake from the collection.

    Args:
        cake_id (int): the identifier of the cake to be removed

    Returns:
        JSONResponse: returns an empty body if the cake has been successfully removed.
    """
    crud.delete_cake(cake_id)

    return JSONResponse(content=None)
