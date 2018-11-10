from rest_framework import serializers
from django.contrib.auth.admin import User
from .models import Advert

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField()


class UserModelSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email', 'password']


class AdvertSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=100)
    price=serializers.IntegerField()

    def create(self, validated_data):
        advert=Advert(**validated_data)
        advert.owner=User.objects.first()
        advert.save()
        return advert

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.save()
        return instance


class AdvertModelSerializer(serializers.Serializer):
    owner=UserModelSerializer(read_only=True)
    class Meta:
        model=Advert
        fields=['id', 'title', 'description', 'price', 'number_view', 'owner']


