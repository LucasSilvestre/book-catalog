from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from alembic import command as alembic_commands
from alembic.config import Config

from app.settings import DB_CONNECTION_STRING

connection_pool = create_engine(DB_CONNECTION_STRING, pool_size=10, max_overflow=0, echo=False)
Session = sessionmaker(bind=connection_pool)
BaseModel = declarative_base()

alembic_configuration = Config('alembic.ini')


class MigrationType(Enum):
    """
        Tipo de comandos disponíveis para execução.
    """
    upgrade = 'upgrade'
    downgrade = 'downgrade'


def run_migration(migration_type: MigrationType, revision: str):
    """
        Executa o comando informado utilizado a API do alembic.

        Exemplo: run_migration(MigrationType.upgrade, 'head')

    :param migration_type: Tipo do comando para execução. Opções disponíveis no enum MigrationType
    :param revision: Revisão alvo.
    :return: None
    """
    getattr(alembic_commands, migration_type.value)(alembic_configuration, revision)


def get_conn():
    conn = Session()
    try:
        yield conn
    except Exception as error:
        raise error
    finally:
        conn.close()
