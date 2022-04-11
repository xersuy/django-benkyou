from datetime import datetime
from xmlrpc.client import boolean
from ninja import Schema, Field


class Customer(Schema):
    customer_id: int
    first_name: str
    last_name: str
    address_id: int
    create_date: datetime
    active: int
    email: str
    store_id: int
    activebool: bool
    last_update: datetime


class CustomerAll(Schema):
    count: int
    data: Customer
