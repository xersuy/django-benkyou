from django.http import JsonResponse
#
from ninja.responses import codes_2xx, codes_3xx, codes_4xx, codes_5xx

# my_codes = frozenset({416, 418, 425, 429, 451})


def JsonSuccess(data, dataType='datas', msg='success'):
    key = dataType
    return JsonResponse({
        "result": {
            "success:": True,
            "message": msg,
            key: data
        }
    })
