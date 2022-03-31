from ninja import NinjaAPI

from user.api import router as user_router


api = NinjaAPI(
    title='Django Ninja Test API',
    version="0.1.0"
)

api.add_router('/user/', user_router)