"""ParkingLot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import (ParkingDetailsView, AddSlotsView, ParkVehicleView,
                    RegistrationNumberForCarsWithColor, SlotNumberForCarsWithColor,
                    SlotNumberForRegistrationNumber, LeaveSlotView)

schema_view_swagger = get_swagger_view(title='Parking Area APIs')

urlpatterns = [
    url(r'^$', schema_view_swagger),
    path('admin/', admin.site.urls),
    path('api/v1/status', ParkingDetailsView.as_view()),
    path('api/v1/addslots', AddSlotsView.as_view()),
    path('api/v1/park', ParkVehicleView.as_view()),
    path('api/v1/registration_numbers_for_cars_with_colour/<color>', RegistrationNumberForCarsWithColor.as_view()),
    path('api/v1/slot_numbers_for_cars_with_colour/<color>', SlotNumberForCarsWithColor.as_view()),
    path('api/v1/slot_number_for_registration_number/<reg_no>', SlotNumberForRegistrationNumber.as_view()),
    path('api/v1/leave', LeaveSlotView.as_view())
]
