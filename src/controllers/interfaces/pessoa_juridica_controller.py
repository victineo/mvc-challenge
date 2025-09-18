from typing import Dict
from abc import ABC, abstractmethod

class PessoaJuridicaControllerInterface(ABC):
    @abstractmethod
    def criar_pessoa_juridica(self, person_info: Dict) -> Dict:
        pass

    @abstractmethod
    def buscar_pessoa_juridica(self, person_id: int) -> Dict:
        pass

    @abstractmethod
    def sacar_dinheiro(self, person_id: int, quantidade: float) -> Dict:
        pass

    @abstractmethod
    def realizar_extrato(self, person_id: int) -> Dict:
        pass
