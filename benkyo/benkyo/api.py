from ninja import NinjaAPI
import simplejson
# import orjson
from user.api import router as user_router
from customer.api import router as customer_router
from ninja.renderers import BaseRenderer


# class NpEncoder(simplejson.JSONEncoder):
#     def default(self, obj):
#         return super(NpEncoder, self).default(obj)


class JSONRenderer (BaseRenderer):

    media_type = 'application/json'

    def render(self, request, data, *, resonse_status):
        return simplejson.dumps(data)

    # def render(self, request, data, *, response_status):
        # return simplejson.dumps(data, cls=NpEncoder, indent=4, ignore_nan=True)


api = NinjaAPI(
    title='Django Ninja text API',
    version="0.1.0",
    renderer=JSONRenderer()
)

api.add_router('/user/', user_router)
api.add_router('/customer/', customer_router)
