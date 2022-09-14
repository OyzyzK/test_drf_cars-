from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import down_file_countries, down_file_producers, down_file_cars, down_file_comments, \
    exportcsv_countries, exportcsv_producers, exportcsv_cars, exportcsv_comments, ProducerViewSet, CommentViewSet, \
    CarsViewSet, CountriesViewSet

router = DefaultRouter()
router.register(r'producers', ProducerViewSet, basename='producer')
router.register(r'comments', CommentViewSet, basename='producer')
router.register(r'cars', CarsViewSet, basename='cars')
router.register(r'countries', CountriesViewSet, basename='producer')

urlpatterns = [
    path('countries/export/', down_file_countries, name='download-xlsx'),
    path('countries/export/csv', exportcsv_countries, name='download-csv'),
    path('producers/export/', down_file_producers, name='download-xlsx'),
    path('producers/export/csv', exportcsv_producers, name='download-csv'),
    path('cars/export/', down_file_cars, name='download-xlsx'),
    path('cars/export/csv', exportcsv_cars, name='download-csv'),
    path('comments/export/', down_file_comments, name='download-xlsx'),
    path('comments/export/csv', exportcsv_comments, name='download-csv'),
    * router.urls
]
