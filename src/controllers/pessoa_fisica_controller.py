from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.pessoa_fisica_controller import PessoaFisicaControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
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
        person_data = self.__pessoa_fisica_repository.create_pessoa_fisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

        return person_data.to_dict()

    def buscar_pessoa_fisica(self, person_id: int) -> Dict:
        person = self.__pessoa_fisica_repository.get_pessoa_fisica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Física não encontrada")

        return person.to_dict()

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> Dict:
        person = self.__pessoa_fisica_repository.withdraw_money(person_id, quantidade)

        return person.to_dict()

    def realizar_extrato(self, person_id: int) -> Dict:
        person = self.__pessoa_fisica_repository.get_pessoa_fisica(person_id)

        return person.to_dict()

    # ----------

    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")
