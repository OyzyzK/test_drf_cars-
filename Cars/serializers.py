from django.db.models import Count
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem


class CountryItemSerializer(ModelSerializer):
    class Meta:
        model = CountryItem
        fields = [
            'name_country',
        ]


class ProducerItemSerializer(ModelSerializer):
    class Meta:
        model = ProducerItem
        fields = ['name_country','name_producer']

    name_country = CountryItemSerializer(read_only=True)

class CommentItemSerializer(ModelSerializer):

    name_producer = SerializerMethodField()
    comment_count = SerializerMethodField()
    class Meta:
        model = CommentItem
        fields = ['name_car','name_producer','comment', 'comment_count']
    read_only_fields = ['name_car']
    def get_comment_count(self,instanse = CommentItem):
        CommentItem.objects.filter(comment=instanse).count()

    def get_name_producer(self,instanse = CommentItem):
        pass

class CarItemSerializer(ModelSerializer):

    comment_count = SerializerMethodField(read_only=True)
    class Meta:
        model = CarItem
        fields = ['name_car', 'name_producer', 'name_country','comment_count']

    name_producer = ProducerItemSerializer(read_only=True)
    name_country = CountryItemSerializer(read_only=True)

    def get_comment_count(self,instanse = CommentItem):
        CommentItem.objects.filter(comment=True).count()