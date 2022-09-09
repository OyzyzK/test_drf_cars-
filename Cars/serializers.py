from rest_framework.serializers import ModelSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem


class ProducerItemSerilixer(ModelSerializer):
    class Meta:
        model = ProducerItem
        fields = ['name', 'country']

class CountryItemSerializer(ModelSerializer):
    class Meta:
        model = CountryItem
        fields = [
            'name'
        ]
