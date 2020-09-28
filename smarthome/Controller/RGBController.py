import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from smarthome.Manager.RGBManager import RGBManager

rgb_manager = RGBManager()


@method_decorator(csrf_exempt)
def rgb_change(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print('loads')
            return JsonResponse({}, status=400)
        token = data.get("token")
        color = data.get("color")
        if token:

            result = rgb_manager.rgb_change(color)
            return HttpResponse(result)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)
