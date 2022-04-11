
from .model import Customer


class CustomerService:
    def __init__(self, engine, session):
        self.engine = engine
        self.session = session
        # self.Customer = Customer

    def customer_all(self):
        return self.session.query(Customer).all()

    def search_customer(self):
        return []
        # self.session.query(Customer).all()
