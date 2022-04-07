from ninja import Router
from .schema import *
from common.db_instance import db_engine, session
from .services import CustomerService

router = Router()


@router.get('/get_cutomer_all/',
            # response=CustomerAll,
            description="Creates an order and updates stock",
            tags=['customer all data'])
#              query = db_engine.execute('select * from customer')
# print(v)
# for v in query:
#     print(v)
def get_customer_all(request):

    all_customer = CustomerService(db_engine, session).customer_all()
    print('[result]', all_customer)

    for i in all_customer:
        print(i)

    return '1'
