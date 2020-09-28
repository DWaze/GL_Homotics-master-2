import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from smarthome.Manager.MotorManager import MotorManager


@method_decorator(csrf_exempt)
def motor_on(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print('loads')
            return JsonResponse({}, status=400)
        token = data.get("token")
        if token:
            motor_manager = MotorManager()
            response = motor_manager.motor_on()
            return HttpResponse(response)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)


@method_decorator(csrf_exempt)
def motor_off(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print('loads')
            return JsonResponse({}, status=400)
        token = data.get("token")
        if token:
            motor_manager = MotorManager()
            response = motor_manager.motor_off()
            return HttpResponse(response)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)
