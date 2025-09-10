from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from sqlalchemy.orm.exc import NoResultFound

class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = PessoaFisica(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_fisica_data)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    def obter_pessoa_fisica(self, person_id: int) -> PessoaFisica | None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = database.session.query(PessoaFisica).filter_by(id=person_id).first()
                return pessoa_fisica_data
            except NoResultFound:
                return None

    def sacar_dinheiro(self, person_id: int, quantidade: float) -> PessoaFisica | None:
        with self.__db_connection as database:
            try:
                pessoa_fisica_data = database.session.query(PessoaFisica).filter_by(id=person_id).first()
                pessoa_fisica_data.saldo -= quantidade
                database.session.commit()
                return pessoa_fisica_data
            except NoResultFound:
                raise ValueError("Pessoa Física não encontrada")
