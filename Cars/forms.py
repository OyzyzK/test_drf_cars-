from rest_framework.fields import SerializerMethodField

from .models import CountryItem, ProducerItem, CarItem, CommentItem
from django.forms import ModelForm



class CountryItemForm(ModelForm):
    class Meta:
        model = CountryItem
        fields = ['name_country']

    def get_name_producer(self):
        pass
class ProducerItemForm(ModelForm):
    class Meta:
        model = ProducerItem
        fields = ['name_producer', 'name_country']


class CarItemForm(ModelForm):
    class Meta:
        model = CarItem
        fields = ['name_car','name_producer', 'year_start', 'year_end']



class CommentItemForm(ModelForm):
    class Meta:
        model = CommentItem
        fields = ['email_name','name_car', 'creation_date', 'comment']