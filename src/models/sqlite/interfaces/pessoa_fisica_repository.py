from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica

class PessoaFisicaRepositoryInterface(ABC):
    @abstractmethod
    def create_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> PessoaFisica:
        pass

    @abstractmethod
    def get_pessoa_fisica(self, person_id: int) -> PessoaFisica | None:
        pass

    @abstractmethod
    def withdraw_money(self, person_id: int, quantidade: float) -> PessoaFisica | None:
        pass
