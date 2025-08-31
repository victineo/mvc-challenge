from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from sqlalchemy.orm.exc import NoResultFound

class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                pessoa_juridica_data = PessoaJuridica(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_juridica_data)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
        
    def get_pessoa_juridica(self, person_id: int) -> PessoaJuridica | None:
        with self.__db_connection as database:
            try:
                pessoa_juridica_data = database.session.query(PessoaJuridica).filter_by(id=person_id).first()
                return pessoa_juridica_data
            except NoResultFound:
                return None
