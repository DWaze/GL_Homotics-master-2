import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from smarthome.Manager.UltrasonicManager import UltrasonicManager


@method_decorator(csrf_exempt)
def ultra_detection(request):
    distance_manager = UltrasonicManager()
    if request.method == 'POST':
        if request.method == 'POST':
            try:
                info = request.body.decode('utf-8')
                data = json.loads(info)
            except ValueError:
                print('loads')
                return JsonResponse({}, status=400)
            token = data.get("token")
            object_id = data.get("id")
            if token:
                print(token)
                print(object_id)

                response = distance_manager.get_distance()
                return HttpResponse(response)
            else:
                return JsonResponse({}, status=401)
        return JsonResponse({}, status=400)
