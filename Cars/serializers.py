from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import CountryItem, ProducerItem, CarItem, CommentItem
from .serialzer_fileds import WriteableRelatedField


class CountryItemSerializer(ModelSerializer):
    class Meta:
        model = CountryItem
        fields = [
            'name_country',
        ]


class ProducerItemSerializer(ModelSerializer):
    class Meta:
        model = ProducerItem
        fields = ['name_producer']


class FullCountrySerializer(ModelSerializer):
    class Meta:
        model = CountryItem
        fields = ['producers', 'name_country']

    producers = ProducerItemSerializer(read_only=True, many=True)


class CarItemSerializer(ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['name_car', 'name_producer', 'year_start', 'year_end']


class SingleCarItemSerializer(ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['name_car']


class FullProducerSerializer(ModelSerializer):
    class Meta:
        model = ProducerItem
        fields = ['cars', 'name_producer', 'name_country', 'comment_count']

    name_country = WriteableRelatedField(serializer=CountryItemSerializer, queryset=CountryItem.objects.all())
    cars = SingleCarItemSerializer(read_only=True, many=True)
    comment_count = SerializerMethodField(read_only=True)

    def get_comment_count(self, instance: ProducerItem):
        return CommentItem.objects.filter(name_car__name_producer=instance).count()


class SingleCommentSerializer(ModelSerializer):
    class Meta:
        model = CommentItem
        fields = ['comment']


class SingleCarSerialzer(ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['name_car']


class FullCarSerialzer(ModelSerializer):
    class Meta:
        model = CarItem
        fields = ['name_car', 'name_producer', 'year_start', 'year_end', 'comments', 'comment_count']
        extra_kwargs = {
            'year_start': {'write_only': True},
            'year_end': {'write_only': True},
        }

    name_producer = WriteableRelatedField(serializer=ProducerItemSerializer, queryset=ProducerItem.objects.all())
    comment_count = SerializerMethodField()
    comments = SingleCommentSerializer(read_only=True, many=True)

    def get_comment_count(self, instance: CarItem):
        return CommentItem.objects.filter(name_car=instance).count()


class CommentItemSerializer(ModelSerializer):
    class Meta:
        model = CommentItem
        fields = ['email_name', 'name_car', 'creation_date', 'comment']

    name_car = WriteableRelatedField(serializer=SingleCarItemSerializer, queryset=CarItem.objects.all())
