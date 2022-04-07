
import os
from common.db_manage import SQLAlchemyManager


db_instance = SQLAlchemyManager(
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME'),
)
