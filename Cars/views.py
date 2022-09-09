from rest_framework import generics

from .serializers import CountryItemSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem



class CountriesJson(generics.ListAPIView):
    queryset = CountryItem.objects.all()
    serializer_class = CountryItemSerializer

#
# class ProducersJson(generics.ListAPIView):
#     queryset = ProducerItem.objects.all()
#     serializer_class = NewsItemSerializer
#
#
# class CarsJson(generics.ListAPIView):
#     queryset = NewsItem.objects.all()
#     serializer_class = NewsItemSerializer
#
#
# class CommentsJson(generics.ListAPIView):
#     queryset = NewsItem.objects.all()
#     serializer_class = NewsItemSerializer



# Create your views here.
