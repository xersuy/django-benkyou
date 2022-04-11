from unittest import result
from django.http import JsonResponse
from ninja.responses import codes_2xx, codes_3xx, codes_4xx, codes_5xx
from ninja import Router
from .schema import *
import pandas as pd
import pendulum
from common.db_instance import db_engine, session
from .services import CustomerService
from common.response_util import JsonSuccess
from common.common_schema import Message

router = Router()


@router.get('/get_cutomer_all/',
            response=None,
            # request={200: CustomerAll, 403: Message},
            description="고객 전체 목록 조회",
            tags=['customer'])
# 유저의 전체 목록을 불러오는 API
# query = db_engine.execute('select * from customer')
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
                'create_date': customer.create_date,
                'active': customer.active,
                'email': customer.email,
                'store_id': customer.store_id,
                'activebool': customer.activebool,
                'last_update': customer.last_update
            }

            customer_dict.append(_customer)

        count = len(customer_dict)
        return JsonResponse({'count': count, 'data': customer_dict})

    else:
        return 402, {'message': '정보조회를 실패했습니다.'}


class SearchCustomerPayload(Schema):
    first_name: str
    last_name: str


@router.post('/search_customer/',
            #  response=SearchCustomerPayload,
             description="고객 유저 이름 검색",
             tags=['customer'])
def search_customer(request, payload: SearchCustomerPayload):
    # first_name = payload.first_name if payload.first_name is not None else ''

    # find = CustomerService(db_engine, session).search_customer()
    # if find:
    #     return JsonSuccess(datas={'data': []}, dataType='datas')
    #     customer_dict = []
    #     # pandas dataframe 을 이용해도 좋을 듯
    #     for customer in all_customer:
    #         _customer = {
    #             'customer_id': customer.customer_id,
    #             'first_name': customer.first_name,
    #             'last_name': customer.last_name,
    #             'address_id': customer.address_id,
    #             'create_date': customer.create_date.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
    #             'active': customer.active,
    #             'email': customer.email,
    #             'store_id': customer.store_id,
    #             'activebool': customer.activebool,
    #             'last_update': customer.last_update.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    #         }

    #         customer_dict.append(_customer)

    #     return JsonSuccess(data={'count': len(customer_dict), 'data': customer_dict}, dataType='datas')

    # else:
    return ''
    # JsonError(msg='error')
