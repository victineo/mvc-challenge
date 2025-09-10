from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaControllerInterface(ABC):
    @abstractmethod
    def criar_pessoa_fisica(self, person_info: Dict) -> Dict:
        pass

    @abstractmethod
    def buscar_pessoa_fisica(self, person_id: int) -> Dict:
        pass
