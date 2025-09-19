from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_controller import PessoaJuridicaControllerInterface
from src.validators.pessoa_juridica_creator_validator import pessoa_juridica_creator_validator

class PessoaJuridicaView:
    def __init__(self, controller: PessoaJuridicaControllerInterface) -> None:
        self.__controller = controller

    def criar_pessoa_juridica(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.criar_pessoa_juridica(person_info)

        return HttpResponse(status_code=201, body=body_response)

    def buscar_pessoa_juridica(self, http_request: HttpRequest) -> HttpResponse:
        try:
            person_id = http_request.param["id"]
            body_response = self.__controller.buscar_pessoa_juridica(person_id)

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
