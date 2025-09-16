from typing import Dict
from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, BIGINT, String, REAL

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"
    
    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_completo = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"PessoaFisica[id={self.id}, nome={self.nome_completo}, email={self.email}]"

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "tipo": "pessoa_fisica",
            "renda_mensal": self.renda_mensal,
            "idade": self.idade,
            "nome_completo": self.nome_completo,
            "celular": self.celular,
            "email": self.email,
            "categoria": self.categoria,
            "saldo": self.saldo
        }
