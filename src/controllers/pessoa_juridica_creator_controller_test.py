import pytest
from .pessoa_juridica_creator_controller import PessoaJuridicaCreatorController

class MockPessoaJuridicaRepository:
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        pass

def test_create():
    person_info = {
        "faturamento": 1000,
        "idade": 30,
        "nome_fantasia": "John Doe",
        "celular": "1234567890",
        "email_corporativo": "john.doe@example.com",
        "categoria": "Categoria A",
        "saldo": 1000
    }

    controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "pessoa_juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "faturamento": 1000,
        "idade": 30,
        "nome_fantasia": "John Doe 123",
        "celular": "1234567890",
        "email_corporativo": "john.doe@example.com",
        "categoria": "A",
        "saldo": 1000
    }

    controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

    with pytest.raises(ValueError):
        controller.create(person_info)
