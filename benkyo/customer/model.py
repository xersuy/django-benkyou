# from django.db import models


from sqlalchemy import ForeignKey, Integer, String, Column, null, Boolean, DateTime

from sqlalchemy.orm import relationship
from common.base import Base


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, comment="고객 번호")
    store_id = Column(Integer, comment="상점 번호")
    first_name = Column(String(45), comment="고객 이름")
    last_name = Column(String(45), comment="고객 성")
    email = Column(String(45),  nullable=True, comment="고객 이메일")
    address_id = Column(Integer, comment="주소 번호")
    #  ForeignKey('Address.address_id')
    activebool = Column(Boolean, comment="고객 상태")
    create_date = Column(DateTime, comment="고객 생성일")
    last_update = Column(DateTime, nullable=True, last_name="고객 수정일")
    active = Column(Integer, nullable=True, comment="고객 상태")


class Address(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True)
    address = Column(String(50))
    address2 = Column(String(50), nullable=True)
    district = Column(String(20))
    # city = Column('City', models.DO_NOTHING)
    city_id = Column(Integer,)
    # ForeignKey('City.city_id')
    postal_code = Column(String(10),  nullable=True)
    phone = Column(String(20))
    last_update = Column(DateTime)

    # class Meta:
    #     managed = False
    #     db_table = 'address'

#
