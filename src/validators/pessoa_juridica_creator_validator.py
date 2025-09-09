from typing import Annotated
from pydantic import BaseModel, StringConstraints, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def pessoa_juridica_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        faturamento: float
        idade: int
        nome_fantasia: Annotated[str, StringConstraints(min_length=4)]
        celular: Annotated[str, StringConstraints(min_length=9, max_length=11)]
        email_corporativo: Annotated[str, StringConstraints(min_length=4)]
        categoria: Annotated[str, StringConstraints(min_length=11, max_length=11)]
        saldo: float
    
    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
