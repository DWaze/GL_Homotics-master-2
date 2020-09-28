import  json
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from smarthome.Manager.GasManager import GasManager


@method_decorator(csrf_exempt)
def gasDetection(request):
    gaz_manager = GasManager()
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

                response = gaz_manager.get_gaz_value()

                return HttpResponse(response)
            else:
                return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)
