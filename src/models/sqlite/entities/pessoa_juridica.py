from typing import Dict
from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, BIGINT, String, REAL

class PessoaJuridica(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=False)
    email_corporativo = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"PessoaJuridica[id={self.id}, nome={self.nome_fantasia}, email={self.email_corporativo}]"

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "tipo": "pessoa_juridica",
            "faturamento": self.faturamento,
            "idade": self.idade,
            "nome_fantasia": self.nome_fantasia,
            "celular": self.celular,
            "email_corporativo": self.email_corporativo,
            "categoria": self.categoria,
            "saldo": self.saldo
        }
