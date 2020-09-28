"""GL_Homotics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from smarthome.Controller import MotorController, GasController, TempController, UltrasonicController, RGBController, RelayController
from .Controller import LightController

urlpatterns = [
    url(r'^light/on', LightController.light_on, name='light On'),
    url(r'^light/off', LightController.light_off, name='light Off'),
    url(r'^motor/on', MotorController.motor_on, name='Montor On'),
    url(r'^motor/off', MotorController.motor_off, name='Montor Off'),
    url(r'^relay/on', RelayController.relay_on, name='Montor On'),
    url(r'^relay/off', RelayController.relay_off, name='Montor Off'),
    url(r'^GasDetection', GasController.gasDetection, name='Gas'),
    url(r'^TempDetection', TempController.temp_detection, name='Temperature'),
    url(r'^UltraDetection', UltrasonicController.ultra_detection, name='Ultrasonic'),
    url(r'^rgbControl', RGBController.rgb_change, name='RGB Led'),
]
