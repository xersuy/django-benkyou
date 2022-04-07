from ninja import Router
from .schema import *
from common.db_instance import db_engine
router = Router()


@router.post('/login/',
             response=LoginSchema,
             description="Creates an order and updates stock",
             tags=['crate_post login'])
def user_login(request, payload: LoginSchema):
    """
    username: str
    """
    query = db_engine.execute('select * from customer')

    for v in query:
        print(v)

    return {
        "username": payload.username,
        "password": payload.password
    }


@router.get('/info/', response=UserInfo, deprecated=True)
def get_user_info(request):

    return {"data": '123123123123'}

# @router.get('/info/', response=UserInfo)
# def get_user_info(request):
#     return {"data": '123123123123'}
