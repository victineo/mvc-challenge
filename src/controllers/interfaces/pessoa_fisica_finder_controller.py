from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass
