from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.pessoa_fisica_finder_controller import PessoaFisicaFinderControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica

class PessoaFisicaFinderController(PessoaFisicaFinderControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
    
    def find(self, person_id: int) -> PessoaFisica | None:
        person = self.__find_pessoa_fisica_in_db(person_id)

        formatted_responde = self.__format_response(person)
        return formatted_responde

    def __find_pessoa_fisica_in_db(self, person_id: int) -> PessoaFisica | None:
        person = self.__pessoa_fisica_repository.get_pessoa_fisica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Física não encontrada")

        return person

    def __format_response(self, person: PessoaFisica | None) -> Dict:
        return {
            "data": {
                "type": "pessoa_fisica",
                "count": 1,
                "attributes": {
                    "renda_mensal": person.renda_mensal,
                    "idade": person.idade,
                    "nome_completo": person.nome_completo,
                    "celular": person.celular,
                    "email": person.email,
                    "categoria": person.categoria,
                    "saldo": person.saldo
                }
            }
        }
