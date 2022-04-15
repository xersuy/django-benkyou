from unittest import result
from django.http import JsonResponse
from ninja.responses import codes_2xx, codes_3xx, codes_4xx, codes_5xx
from ninja import Router
from .schema import *
import pandas as pd
import pendulum
from common.db_instance import db_engine, session
from .services import CustomerService
from common.common_schema import Message
from .schema import CustomerAll, CustomerFirst
router = Router()


@router.get('/get_cutomer_all/',
            # swagger에 디스크립션 형태로 들어가는 부분
            response={200: CustomerAll, 401: Message, 402: Message},
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
        return JsonResponse({'count': count, 'data': customer_dict}, status=200)

    else:
        return JsonResponse({'message': '정보조회를 실패했습니다.'}, status=401)


class SearchCustomerPayload(Schema):
    first_name: str


@router.post('/search_first/',
             response={200: CustomerFirst, 401: Message, 402: Message},
             description="고객 유저 이름 검색",
             tags=['customer'])
def search_firstname(request, payload: SearchCustomerPayload):
    first_name = payload.first_name if payload.first_name is not None else ''

    if first_name == '':
        return JsonResponse({'message': '값을 정확히 입력해주세요'}, status=402)

    customers = CustomerService(db_engine, session).customer_firstname(
        first_name=first_name,
    )

    _customer = []
    for customer in customers:
        temp = {
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
        _customer.append(temp)

    if _customer:
        return JsonResponse({'data': _customer}, status=200)
    else:
        return JsonResponse({'message': '정보조회를 실패했습니다.'}, status=401)
