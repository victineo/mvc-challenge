from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.pessoa_juridica_finder_controller import PessoaJuridicaFinderControllerInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica

class PessoaJuridicaFinderController(PessoaJuridicaFinderControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository
    
    def find(self, person_id: int) -> PessoaJuridica | None:
        person = self.__find_pessoa_juridica_in_db(person_id)

        formatted_responde = self.__format_response(person)
        return formatted_responde

    def __find_pessoa_juridica_in_db(self, person_id: int) -> PessoaJuridica | None:
        person = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Jurídica não encontrada")

        return person

    def __format_response(self, person: PessoaJuridica | None) -> Dict:
        return {
            "data": {
                "type": "pessoa_juridica",
                "count": 1,
                "attributes": {
                    "faturamento": person.faturamento,
                    "idade": person.idade,
                    "nome_fantasia": person.nome_fantasia,
                    "celular": person.celular,
                    "email_corporativo": person.email_corporativo,
                    "categoria": person.categoria,
                    "saldo": person.saldo
                }
            }
        }
