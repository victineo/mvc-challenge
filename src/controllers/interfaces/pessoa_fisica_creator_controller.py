from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, person_info: Dict) -> None:
        pass
