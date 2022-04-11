from ninja import NinjaAPI
import pendulum
import json
import simplejson
import numpy
import datetime
# import orjson
from user.api import router as user_router
from customer.api import router as customer_router
from ninja.renderers import BaseRenderer


# class NpEncoder(simplejson.JSONEncoder):
#     def default(self, obj):
#         return super(NpEncoder, self).default(obj)


class NpEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (numpy.integer, numpy.int_, numpy.intc, numpy.intp, numpy.int8,
                            numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
                            numpy.uint16, numpy.uint32, numpy.uint64)):
            return int(obj)
        if isinstance(obj, (numpy.floating, numpy.float_, numpy.float16, numpy.float32, numpy.float64)):
            return float(obj)
        if isinstance(obj, (numpy.bool_)):
            return bool(obj)
        if isinstance(obj, (numpy.void)):
            return None
        if isinstance(obj, float) and numpy.isnan(obj):
            return None
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        if isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return super().default(obj)


class NumpyJSONRenderer(BaseRenderer):
    media_type = 'application/json'

    def render(self, request, data, *, response_status):
        return simplejson.dumps(data, cls=NpEncoder, indent=4, ignore_nan=True)


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
