from ninja import NinjaAPI

from user.api import router as user_router
from customer.api import router as customer_router

api = NinjaAPI(
    title='Django Ninja text API',
    version="0.1.0"
)

api.add_router('/user/', user_router)
api.add_router('/customer/', customer_router)
