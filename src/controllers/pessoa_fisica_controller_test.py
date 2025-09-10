import pytest
from .pessoa_fisica_controller import PessoaFisicaController

class MockPessoaFisica():
    def __init__(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo

class MockPessoaFisicaRepository:
    def criar_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        pass

    def buscar_pessoa_fisica(self, person_id: int) -> MockPessoaFisica | None:
        return MockPessoaFisica(
            renda_mensal=5000,
            idade=35,
            nome_completo="João da Silva",
            celular="9999-8888",
            email="joao@example.com",
            categoria="Categoria A",
            saldo=10000
        )

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> MockPessoaFisica | None:
        person_mock = MockPessoaFisica(
            renda_mensal=5000,
            idade=35,
            nome_completo="João da Silva",
            celular="9999-8888",
            email="joao@example.com",
            categoria="Categoria A",
            saldo=10000
        )

        person_mock.saldo -= quantidade
        return person_mock

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

    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    response = controller.criar_pessoa_fisica(person_info)

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

    controller = PessoaFisicaController(MockPessoaFisicaRepository())

    with pytest.raises(ValueError):
        controller.criar_pessoa_fisica(person_info)

def test_find():
    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    response = controller.buscar_pessoa_fisica(1)

    expected_response = {
        "data": {
            "type": "pessoa_fisica",
            "count": 1,
            "attributes": {
                "renda_mensal": 5000,
                "idade": 35,
                "nome_completo": "João da Silva",
                "celular": "9999-8888",
                "email": "joao@example.com",
                "categoria": "Categoria A",
                "saldo": 10000
            }
        }
    }

    assert response == expected_response

def test_sacar_dinheiro():
    controller = PessoaFisicaController(MockPessoaFisicaRepository())
    response = controller.sacar_dinheiro(1, 1000)

    assert response["data"]["type"] == "pessoa_fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["saldo"] == 9000
