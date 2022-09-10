from django.urls import path
from .views import CountryPOSTDELADD, CountryGET, ProducerGET

urlpatterns = [
                  path('countries/',CountryGET.as_view()),
                  path('producers/', ProducerGET.as_view()),
                  #path('delete_country/', delete_country, name='delete_country')
              ]