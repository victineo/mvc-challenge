from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.pessoa_juridica_controller import PessoaJuridicaControllerInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
import re

class PessoaJuridicaController(PessoaJuridicaControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def criar_pessoa_juridica(self, person_info: Dict) -> None:
        faturamento = person_info['faturamento']
        idade = person_info['idade']
        nome_fantasia = person_info['nome_fantasia']
        celular = person_info['celular']
        email_corporativo = person_info['email_corporativo']
        categoria = person_info['categoria']
        saldo = person_info['saldo']

        self.__validate_complete_name(nome_fantasia)
        self.__insert_pessoa_juridica_in_db(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

        return self.__format_response(person_info)

    def buscar_pessoa_juridica(self, person_id: int) -> Dict:
        person = self.__find_pessoa_juridica_in_db(person_id)

        formatted_responde = self.__format_response(person)
        return formatted_responde

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> Dict:
        person = self.__sacar_dinheiro_in_db(person_id, quantidade)

        return self.__format_response(person)

    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")

    def __insert_pessoa_juridica_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        self.__pessoa_juridica_repository.create_pessoa_juridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

    def __find_pessoa_juridica_in_db(self, person_id: int) -> PessoaJuridica | None:
        person = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Jurídica não encontrada")

        return person

    def __sacar_dinheiro_in_db(self, person_id: int, quantidade: float) -> PessoaJuridica | None:
        person = self.__pessoa_juridica_repository.withdraw_money(person_id, quantidade)

        if not person:
            raise HttpNotFoundError("Pessoa Jurídica não encontrada")

        return person

    def __format_response(self, person: PessoaJuridica | Dict | None) -> Dict:
        if isinstance(person, Dict):
            return {
                "data": {
                    "type": "pessoa_juridica",
                    "count": 1,
                    "attributes": person
                }
            }

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
