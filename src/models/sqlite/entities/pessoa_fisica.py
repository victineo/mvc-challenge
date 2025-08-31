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
