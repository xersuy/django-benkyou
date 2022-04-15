from datetime import datetime
from ninja import Schema
from typing import List, Dict, Optional


class Customer(Schema):
    customer_id: int
    first_name: str
    last_name: str
    address_id: int
    create_date: str
    active: int
    email: str
    store_id: int
    activebool: bool
    last_update: str


class CustomerAll(Schema):
    count: int
    data: List[Customer]


class CustomerFirst(Schema):
    data: List[Customer]
