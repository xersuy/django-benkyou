from django.http import JsonResponse


def JsonSuccess(data, dataType='datas', msg='success'):
    key = dataType
    return JsonResponse({
        "result": {
            "success:": True,
            "message": msg,
            key: data
        }
    })


def JsonError(msg='error'):
    return JsonResponse({
        "result": {
            "success:": False,
            "message": msg,
        }
    })
