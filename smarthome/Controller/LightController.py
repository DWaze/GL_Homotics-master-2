import json

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from smarthome.Manager.LightManager import LightManager


@method_decorator(csrf_exempt)
def light_on(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({}, status=400)
        token = data.get("token")
        if token:
            light_manager = LightManager()
            response = light_manager.light_on()
            return HttpResponse(response)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)


@method_decorator(csrf_exempt)
def light_off(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({}, status=400)
        token = data.get("token")
        if token:
            light_manager = LightManager()
            response = light_manager.light_off()
            return HttpResponse(response)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)
