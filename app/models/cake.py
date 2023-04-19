from models.base_models import CamelModel
from pydantic import conint, constr


class CakeApi(CamelModel):
    """Model of a cake for the API interface."""

    comment: constr(max_length=200)
    id: int
    image_url: str
    name: constr(max_length=30)
    yum_factor: conint(ge=1, le=5)
