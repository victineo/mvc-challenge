from typing import Dict
from .interfaces.pessoa_juridica_creator_controller import PessoaJuridicaCreatorControllerInterface
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
import re

class PessoaJuridicaCreatorController(PessoaJuridicaCreatorControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository
    
    def create(self, person_info: Dict) -> None:
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
    
    def __validate_complete_name(self, complete_name: str) -> None:
        valid_characters = re.compile(r'^[a-zA-Z\s]+$')

        if not valid_characters.search(complete_name):
            raise ValueError("Nome completo deve conter apenas letras e espaços")
    
    def __insert_pessoa_juridica_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        self.__pessoa_juridica_repository.create_pessoa_juridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
    
    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "pessoa_juridica",
                "count": 1,
                "attributes": person_info
            }
        }
