from urllib.parse import quote
import sqlalchemy


class SQLAlchemyManager:
    def __init__(self, user, password, host, port, dbname):
        self.engine = self.create_engine(user, password, host, port, dbname)

    @staticmethod
    def create_engine(user, password, host, port, dbname):
        url = 'postgresql://{}:%s@{}:{}/{}'.format(
            user, host, port, dbname) % quote(password)

        return sqlalchemy.create_engine(
            url, client_encoding='utf8')
