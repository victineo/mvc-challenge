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
        person_data = self.__pessoa_juridica_repository.create_pessoa_juridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

        return person_data.to_dict()

    def buscar_pessoa_juridica(self, person_id: int) -> Dict:
        person = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)

        if not person:
            raise HttpNotFoundError("Pessoa Jurídica não encontrada")

        return person.to_dict()

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> Dict:
        person = self.__pessoa_juridica_repository.withdraw_money(person_id, quantidade)

        return person.to_dict()

    # ----------

    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")
