from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica

class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def criar_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        pass

    @abstractmethod
    def obter_pessoa_juridica(self, person_id: int) -> PessoaJuridica | None:
        pass
