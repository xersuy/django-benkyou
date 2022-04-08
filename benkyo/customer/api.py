from unittest import result
from ninja import Router
from .schema import *
import pandas as pd
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

    if all_customer:
        customer_dict = []

        for customer in all_customer:
            _customer = {
                'customer_id': customer.customer_id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                # 'address_id': customer.address_id,
                'create_date': customer.create_date,
                'active': customer.active,
                'email': customer.email,
                'store_id': customer.store_id,
                'activebool': customer.activebool,
                'last_update': customer.last_update,
            }
            # print(_customer)

            customer_dict.append(_customer)

        cusotomers_df = pd.DataFrame(all_customer)
        print(cusotomers_df)
        return {
            'result': cusotomers_df
        }

    else:
        print('------------------------------->')
    # print(all_customer)
    # print(cusotomers_df)
    # return all_customer
    # print('[result]', all_customer)
    # result = [{"name": v.first_name, "last_name": v.last_name,
    #            "email": v.email, "address": v.address} for v in all_customer]

    # for i in result:
    # print(i)

    # return Response({
    #     'result': all_customer
    # })
