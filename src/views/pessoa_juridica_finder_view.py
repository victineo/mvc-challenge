from .interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pessoa_juridica_finder_controller import PessoaJuridicaFinderControllerInterface

class PessoaJuridicaFinderView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["id"]
        body_response = self.__controller.find(person_id)

        return HttpResponse(status_code=200, body=body_response)
