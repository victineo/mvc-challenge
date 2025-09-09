from .pessoa_fisica_finder_controller import PessoaFisicaFinderController

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
    def get_pessoa_fisica(self, person_id: int) -> MockPessoaFisica | None:
        return MockPessoaFisica(
            renda_mensal=5000,
            idade=35,
            nome_completo="João da Silva",
            celular="9999-8888",
            email="joao@example.com",
            categoria="Categoria A",
            saldo=10000
        )

def test_find():
    controller = PessoaFisicaFinderController(MockPessoaFisicaRepository())
    response = controller.find(1)

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
