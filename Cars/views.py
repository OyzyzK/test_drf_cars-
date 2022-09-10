from django.shortcuts import redirect, render
from rest_framework import generics

from .serializers import CountryItemSerializer, ProducerItemSerilizer, CarItemSerializer, CommentItemSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem


class CountryPOSTDELADD:

    def add_country(request, event_id):
        pass


    def edit_country(request, event_id):
        pass


    def delete_country(request, event_id):
        event = CountryItem.objects.get(pk=event_id)
        event.delete()
        return redirect('countries')

class CountryGET(generics.ListAPIView):
    queryset = ProducerItem.objects.all()
    serializer_class = ProducerItemSerilizer

class ProducerGET(generics.ListAPIView):
    queryset = ProducerItem.objects.all()
    serializer_class = ProducerItemSerilizer


class CarsGET(generics.ListAPIView):
     queryset = CarItem.objects.all()
     serializer_class = CarItemSerializer

class CommentsGET(generics.ListAPIView):
     queryset = CommentItem.objects.all()
     serializer_class = CommentItemSerializer


# Create your views here.
