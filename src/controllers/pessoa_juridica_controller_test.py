from typing import Dict
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

    def to_dict(self) -> Dict:
        return {
            "id": 1,
            "tipo": "pessoa_juridica",
            "faturamento": self.faturamento,
            "idade": self.idade,
            "nome_fantasia": self.nome_fantasia,
            "celular": self.celular,
            "email_corporativo": self.email_corporativo,
            "categoria": self.categoria,
            "saldo": self.saldo
        }

class MockPessoaJuridicaRepository:
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> MockPessoaJuridica:
        return MockPessoaJuridica(
            faturamento=faturamento,
            idade=idade,
            nome_fantasia=nome_fantasia,
            celular=celular,
            email_corporativo=email_corporativo,
            categoria=categoria,
            saldo=saldo
        )

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
            saldo=70000 - quantidade
        )

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

    assert response["tipo"] == "pessoa_juridica"
    for key, value in legal_entity_info.items():
        assert response[key] == value

def test_create_error():
    legal_entity_info = {
        "faturamento": 90000,
        "idade": 15,
        "nome_fantasia": "Empresa ABC 123",
        "celular": "1234-5678",
        "email_corporativo": "contato@abc123.com",
        "categoria": "B",
        "saldo": 40000
    }

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())

    with pytest.raises(ValueError):
        controller.criar_pessoa_juridica(legal_entity_info)

def test_find():
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.buscar_pessoa_juridica(1)

    expected_response = {
        "id": 1,
        "tipo": "pessoa_juridica",
        "faturamento": 80000,
        "idade": 5,
        "nome_fantasia": "Empresa ABC",
        "celular": "5555-6666",
        "email_corporativo": "contato@abc.com",
        "categoria": "Categoria B",
        "saldo": 70000
    }

    assert response == expected_response

def test_sacar_dinheiro():
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.sacar_dinheiro(1, 1000)

    assert response["saldo"] == 69000
