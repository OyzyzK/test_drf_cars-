from rest_framework import serializers


class WriteableRelatedField(serializers.PrimaryKeyRelatedField):
    def __init__(self, serializer, **kwargs):
        super().__init__(**kwargs)
        self.serializer = serializer

    def to_representation(self, value):
        obj = self.serializer.Meta.model.objects.get(id=str(value))
        return self.serializer(obj).data
