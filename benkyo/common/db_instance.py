
import os
from common.db_manage import SQLAlchemyManager
from sqlalchemy.orm import scoped_session, sessionmaker


db_instance = SQLAlchemyManager(
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME'),
)

# sqlalchemy engine
db_engine = db_instance.engine

# sqlalchemy session
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=db_engine))
