from unittest import result

from ninja import Router
from .schema import *
import pandas as pd
import pendulum
from common.db_instance import db_engine, session
from .services import CustomerService
from common.response_util import JsonSuccess, JsonError
router = Router()


@router.get('/get_cutomer_all/',
            response=CustomerAll,
            description="유저 전체 목록 조회",
            tags=['customer all data'])
# 유저의 전체 목록을 불러오는 API              query = db_engine.execute('select * from customer')
def get_customer_all(request):
    all_customer = CustomerService(db_engine, session).customer_all()
    if all_customer:
        customer_dict = []
        # pandas dataframe 을 이용해도 좋을 듯
        for customer in all_customer:
            _customer = {
                'customer_id': customer.customer_id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'address_id': customer.address_id,
                'create_date': customer.create_date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
                'active': customer.active,
                'email': customer.email,
                'store_id': customer.store_id,
                'activebool': customer.activebool,
                'last_update': customer.last_update.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            }

            customer_dict.append(_customer)

        count = len(customer_dict)

        return JsonSuccess(data={'count': count, 'data': customer_dict}, dataType='datas')

    else:
        return JsonError(msg='error')
