import pytest
from .pessoa_fisica_creator_controller import PessoaFisicaCreatorController

class MockPessoaFisicaRepository:
    def create_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        pass

def test_create():
    person_info = {
        "renda_mensal": 1000,
        "idade": 30,
        "nome_completo": "John Doe",
        "celular": "1234567890",
        "email": "john.doe@example.com",
        "categoria": "Categoria A",
        "saldo": 1000
    }

    controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "pessoa_fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "renda_mensal": 1000,
        "idade": 30,
        "nome_completo": "John Doe 123",
        "celular": "1234567890",
        "email": "john.doe@example.com",
        "categoria": "A",
        "saldo": 1000
    }

    controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())

    with pytest.raises(ValueError):
        controller.create(person_info)
