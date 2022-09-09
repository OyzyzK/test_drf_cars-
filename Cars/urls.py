from django.urls import path
from .views import CountriesJson

urlpatterns = [
                  path('countries/',CountriesJson.as_view()),
              ]