import humps
from pydantic import BaseModel


class CamelModel(BaseModel):
    class Config:
        """Model which allows the camelize-d alias to be used for the fields.

        Ref: https://github.com/nficano/humps#usage
        """

        alias_generator = humps.camelize
        allow_population_by_field_name = True
