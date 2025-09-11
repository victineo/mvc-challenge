import pytest
from .pessoa_juridica_controller import PessoaJuridicaController

class MockPessoaJuridica():
    def __init__(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        self.faturamento = faturamento
        self.idade = idade
        self.nome_fantasia = nome_fantasia
        self.celular = celular
        self.email_corporativo = email_corporativo
        self.categoria = categoria
        self.saldo = saldo

class MockPessoaJuridicaRepository:
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        pass

    def get_pessoa_juridica(self, person_id: int) -> MockPessoaJuridica | None:
        return MockPessoaJuridica(
            faturamento=80000,
            idade=5,
            nome_fantasia="Empresa ABC",
            celular="5555-6666",
            email_corporativo="contato@abc.com",
            categoria="Categoria B",
            saldo=70000
        )

    def withdraw_money(self, person_id: int, quantidade: float) -> MockPessoaJuridica | None:
        legal_entity_mock = MockPessoaJuridica(
            faturamento=80000,
            idade=5,
            nome_fantasia="Empresa ABC",
            celular="5555-6666",
            email_corporativo="contato@abc.com",
            categoria="Categoria B",
            saldo=70000
        )

        legal_entity_mock.saldo -= quantidade
        return legal_entity_mock

def test_create():
    legal_entity_info = {
        "faturamento": 80000,
        "idade": 5,
        "nome_fantasia": "Empresa ABC",
        "celular": "5555-6666",
        "email_corporativo": "contato@abc.com",
        "categoria": "Categoria B",
        "saldo": 70000
    }

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.criar_pessoa_juridica(legal_entity_info)

    assert response["data"]["type"] == "pessoa_juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == legal_entity_info

def test_create_error():
    legal_entity_info = {
        "faturamento": 1000,
        "idade": 30,
        "nome_fantasia": "Empresa ABC 123",
        "celular": "1234-5678",
        "email_corporativo": "contato@abc123.com",
        "categoria": "B",
        "saldo": 1000
    }

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())

    with pytest.raises(ValueError):
        controller.criar_pessoa_juridica(legal_entity_info)

def test_find():
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.buscar_pessoa_juridica(2)

    expected_response = {
        "data": {
            "type": "pessoa_juridica",
            "count": 1,
            "attributes": {
                "faturamento": 80000,
                "idade": 5,
                "nome_fantasia": "Empresa ABC",
                "celular": "5555-6666",
                "email_corporativo": "contato@abc.com",
                "categoria": "Categoria B",
                "saldo": 70000
            }
        }
    }

    assert response == expected_response

def test_sacar_dinheiro():
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.sacar_dinheiro(2, 1000)

    assert response["data"]["type"] == "pessoa_juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["saldo"] == 69000
