from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.pessoa_fisica_controller import PessoaFisicaControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
import re

class PessoaFisicaController(PessoaFisicaControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def criar_pessoa_fisica(self, person_info: Dict) -> Dict:
        renda_mensal = person_info['renda_mensal']
        idade = person_info['idade']
        nome_completo = person_info['nome_completo']
        celular = person_info['celular']
        email = person_info['email']
        categoria = person_info['categoria']
        saldo = person_info['saldo']

        self.__validate_complete_name(nome_completo)
        self.__insert_pessoa_fisica_in_db(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

        return self.__format_response(person_info)

    def buscar_pessoa_fisica(self, person_id: int) -> Dict:
        person = self.__find_pessoa_fisica_in_db(person_id)

        formatted_response = self.__format_response(person)
        return formatted_response

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> Dict:
        person = self.__sacar_dinheiro_in_db(person_id, quantidade)

        return self.__format_response(person)

    # -----

    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")

    def __insert_pessoa_fisica_in_db(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.__pessoa_fisica_repository.create_pessoa_fisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    def __find_pessoa_fisica_in_db(self, person_id: int) -> PessoaFisica | None:
        person = self.__pessoa_fisica_repository.get_pessoa_fisica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Física não encontrada")

        return person

    def __sacar_dinheiro_in_db(self, person_id: int, quantidade: float) -> PessoaFisica | None:
        person = self.__pessoa_fisica_repository.withdraw_money(person_id, quantidade)

        if not person:
            raise HttpNotFoundError("Pessoa Física não encontrada")

        return person

    def __format_response(self, person: PessoaFisica | Dict | None) -> Dict:
        if isinstance(person, Dict):
            return {
                "data": {
                    "type": "pessoa_fisica",
                    "count": 1,
                    "attributes": person
                }
            }

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
