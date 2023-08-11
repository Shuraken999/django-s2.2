from django.urls import path

from measurement.views import MeasurementView, SensorView, SensorUpdate, SensorsView, SensorCreate

urlpatterns = [
    path('sensors/<pk>/', SensorView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('sensors-upd/<pk>/', SensorUpdate.as_view()),
    path('measurements-upd/', MeasurementView.as_view()),
    path('sensors-cr/', SensorCreate.as_view()),
]
