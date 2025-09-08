from typing import Dict
from .interfaces.pessoa_fisica_creator_controller import PessoaFisicaCreatorControllerInterface
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
import re

class PessoaFisicaCreatorController(PessoaFisicaCreatorControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
    
    def create(self, person_info: Dict) -> None:
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
    
    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")
    
    def __insert_pessoa_fisica_in_db(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.__pessoa_fisica_repository.create_pessoa_fisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
    
    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "pessoa_fisica",
                "count": 1,
                "attributes": person_info
            }
        }
