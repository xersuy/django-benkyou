from ninja import Router, Schema
from django.http import HttpResponse

router = Router()


class UserInfo(Schema):
    data: str


@router.get('/info/', response=UserInfo)
def get_user_info(request):
    return {"data": '123123123123'}
