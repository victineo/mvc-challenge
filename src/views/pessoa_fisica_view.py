from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_fisica_controller import PessoaFisicaControllerInterface
from src.validators.pessoa_fisica_creator_validator import pessoa_fisica_creator_validator

class PessoaFisicaView:
    def __init__(self, controller: PessoaFisicaControllerInterface) -> None:
        self.__controller = controller

    def criar_pessoa_fisica(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.criar_pessoa_fisica(person_info)

        return HttpResponse(status_code=201, body=body_response)

    def buscar_pessoa_fisica(self, http_request: HttpRequest) -> HttpResponse:
        try:
            person_id = http_request.param["id"]
            body_response = self.__controller.buscar_pessoa_fisica(person_id)

            return HttpResponse(status_code=201, body=body_response)
        except ValueError as e:
            return HttpResponse(status_code=400, body=str(e))

    def sacar_dinheiro(self, http_request: HttpRequest) -> HttpResponse:
        try:
            person_id = http_request.param["id"]
            quantidade = http_request.body["quantidade"]
            body_response = self.__controller.sacar_dinheiro(person_id, quantidade)

            return HttpResponse(status_code=201, body=body_response)
        except ValueError as e:
            return HttpResponse(status_code=400, body=str(e))

    def realizar_extrato(self, http_request: HttpRequest) -> HttpResponse:
        try:
            person_id = http_request.param["id"]
            body_response = self.__controller.realizar_extrato(person_id)

            return HttpResponse(status_code=201, body=body_response)
        except ValueError as e:
            return HttpResponse(status_code=400, body=str(e))
