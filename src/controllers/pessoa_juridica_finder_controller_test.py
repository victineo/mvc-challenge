from .pessoa_juridica_finder_controller import PessoaJuridicaFinderController

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
    def get_pessoa_juridica(self, person_id: int) -> MockPessoaJuridica | None:
        return MockPessoaJuridica(
            faturamento=100000,
            idade=10,
            nome_fantasia="Empresa XYZ",
            celular="1111-2222",
            email_corporativo="contato@empresa.com",
            categoria="Categoria A",
            saldo=50000
        )

def test_find():
    controller = PessoaJuridicaFinderController(MockPessoaJuridicaRepository())
    response = controller.find(1)

    expected_response = {
        "data": {
            "type": "pessoa_juridica",
            "count": 1,
            "attributes": {
                "faturamento": 100000,
                "idade": 10,
                "nome_fantasia": "Empresa XYZ",
                "celular": "1111-2222",
                "email_corporativo": "contato@empresa.com",
                "categoria": "Categoria A",
                "saldo": 50000
            }
        }
    }

    assert response == expected_response
