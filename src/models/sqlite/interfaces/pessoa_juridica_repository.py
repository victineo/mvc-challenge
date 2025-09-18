from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica

class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> PessoaJuridica:
        pass

    @abstractmethod
    def get_pessoa_juridica(self, legal_entity_id: int) -> PessoaJuridica | None:
        pass

    @abstractmethod
    def withdraw_money(self, legal_entity_id: int, quantidade: float) -> PessoaJuridica | None:
        pass
