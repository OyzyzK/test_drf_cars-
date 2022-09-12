from django.urls import path
from .views import CountryGET, ProducerGET, CarsGET, create_country, CountriesUpadateView, CountriesDeleteView, \
    index_country, \
    index_producer, create_producer, ProducersUpadateView, ProducersDeleteView, index_car, create_car, index_comment, \
    create_comment, CarsUpadateView, CarsDeleteView, CommentsUpadateView, CommentsDeleteView

urlpatterns = [
    path('countries/', CarsGET.as_view()),
    path('countries/', index_country),
    path('countries_create/', create_country),
    path('countries/update/<int:pk>', CountriesUpadateView.as_view(), name = 'countries-update'),
    path('countries/delete/<int:pk>', CountriesDeleteView.as_view(), name='countries-delete'),

    path('producers/', index_producer),
    path('producers_create/', create_producer),
    path('producers/update/<int:pk>', ProducersUpadateView.as_view(), name='producers-update'),
    path('producers/delete/<int:pk>', ProducersDeleteView.as_view(), name='producers-delete'),

    path('cars/', index_car),
    path('cars_create/', create_car),
    path('cars/update/<int:pk>', CarsUpadateView.as_view(), name='cars-update'),
    path('cars/delete/<int:pk>', CarsDeleteView.as_view(), name='cars-delete'),

    path('comments/', index_comment),
    path('comments_create/', create_comment),
    path('comments/update/<int:pk>', CommentsUpadateView.as_view(), name='comments-update'),
    path('comments/delete/<int:pk>', CommentsDeleteView.as_view(), name='comments-delete')

]
