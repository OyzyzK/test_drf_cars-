from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from rest_framework import generics
from .forms import CountryItemForm, ProducerItemForm, CarItemForm, CommentItemForm
from .serializers import ProducerItemSerializer, CarItemSerializer, CommentItemSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem


def index_country(request):
    context = dict(
        country_items=CountryItem.objects.all()
    )
    return render(request, 'countries.html', context)


class CountriesDeleteView(DeleteView):
    model = CountryItem
    template_name = 'country_del.html'
    success_url = 'http://127.0.0.1:8000/api/countries/'
    fields = ['name_country']


class CountriesUpadateView(UpdateView):
    model = CountryItem
    template_name = 'country_add.html'
    fields = ['name_country']


def create_country(request):
    error = ''
    if request.method == 'POST':
        form = CountryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/api/countries/')
        else:
            error = 'error'

    form = CountryItemForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'country_add.html', data)


def index_producer(request):
    context = dict(
        producer_items=ProducerItem.objects.all()
    )
    return render(request, 'producers.html', context)

class ProducersDeleteView(DeleteView):
    model = ProducerItem
    template_name = 'producer_del.html'
    success_url = 'http://127.0.0.1:8000/api/producers/'
    fields = ['name_producer','name_country']


class ProducersUpadateView(UpdateView):
    model = ProducerItem
    template_name = 'producer_add.html'
    fields = ['name_producer','name_country']


def create_producer(request):
    error = ''
    if request.method == 'POST':
        form = ProducerItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/api/producers/')
        else:
            error = 'error'

    form = ProducerItemForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'producer_add.html', data)

def index_car(request):
    context = dict(
        car_items=CarItem.objects.all()
    )
    return render(request, 'cars.html', context)

class CarsDeleteView(DeleteView):
    model = CarItem
    template_name = 'cars_del.html'
    success_url = 'http://127.0.0.1:8000/api/cars/'
    fields = ['name_car','name_producer', 'year_start', 'year_end']


class CarsUpadateView(UpdateView):
    model = CarItem
    template_name = 'car_add.html'
    fields = ['name_car','name_producer', 'year_start', 'year_end']


def create_car(request):
    error = ''
    if request.method == 'POST':
        form = CarItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/api/cars/')
        else:
            error = 'error'

    form = CarItemForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cars_add.html', data)

def index_comment(request):
    context = dict(
        comment_items=CommentItem.objects.all()
    )
    return render(request, 'comments.html', context)


class CommentsDeleteView(DeleteView):
    model = CommentItem
    template_name = 'comments_del.html'
    success_url = 'http://127.0.0.1:8000/api/comments/'
    fields = ['email_name','name_car', 'creation_date', 'comment']


class CommentsUpadateView(UpdateView):
    model = CommentItem
    template_name = 'comments_add.html'
    fields = ['email_name','name_car', 'creation_date', 'comment']

def create_comment(request):
    error = ''
    if request.method == 'POST':
        form = CommentItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/api/comments/')
        else:
            error = 'error'

    form = CommentItemForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'comments_add.html', data)


class CountryGET(generics.ListAPIView):
    queryset = ProducerItem.objects.all()
    serializer_class = ProducerItemSerializer


class ProducerGET(generics.ListAPIView):
    queryset = CarItem.objects.all()
    serializer_class = CarItemSerializer


class CarsGET(generics.ListAPIView):
    queryset = CommentItem.objects.all()
    serializer_class = CommentItemSerializer

# Create your views here.
