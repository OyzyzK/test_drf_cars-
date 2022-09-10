from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem



class CountryItemSerializer(ModelSerializer):
    class Meta:
        model = CountryItem
        fields = [
            'country',
        ]

class ProducerItemSerilizer(ModelSerializer):
    class Meta:
        model = ProducerItem
        fields = ['name_p', 'country']
    country = CountryItemSerializer(read_only=True)

class CarItemSerializer(ModelSerializer):
    pass
    # class Meta:
    #     model = ProducerItem
    #     fields = ['name_p', 'country']
    # country = CountryItemSerializer(read_only=True)


class CommentItemSerializer(ModelSerializer):
    pass
    # class Meta:
    #     model = ProducerItem
    #     fields = ['name_p', 'country']
    # country = CountryItemSerializer(read_only=True)






#производителя у страны
