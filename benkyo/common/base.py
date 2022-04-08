from sqlalchemy.orm import declarative_base

Base = declarative_base()

# PostgreSQL 사용 시 기본 스키마 지정
# SCHEMA_NAME = 'news_data'
# Base.__table_args__ = {
# 'schema': SCHEMA_NAME,
# }
