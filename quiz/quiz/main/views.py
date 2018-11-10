from django.http import HttpResponse, Http404
from .serializers import UserSerializer, UserModelSerializer, AdvertSerializer, AdvertModelSerializer
from .models import Advert
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.


class AdvertList(APIView):
    def get(self, request):
        adverts=Advert.objects.all()
        serializer=AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=AdvertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AdvertDetail(APIView):
    def get_object(self, pk):
        try:
            return Advert.objects.get(id=pk)
        except Advert.DoesNotExist:
            return Http404

    def get(self, request, pk):
        advert=self.get_object(pk)
        serializer=AdvertModelSerializer(advert)
        return Response(serializer.data)

    def put(self, request, pk):
        advert=self.get_object(pk)
        serializer=AdvertSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advert=self.get_object(pk)
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})
    token, created=Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def register(request):
    serializer=UserModelSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(request.data.get('username'), request.data.get('email'), request.data.get('password'))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view
def advert_list(request):
    if request.method=='GET':
        adverts = Advert.objects.all()
        serializer = AdvertModelSerializer(adverts, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = AdvertModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def advert_detail(request, pk):
    try:
        advert=Advert.objects.get(id=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = AdvertModelSerializer(advert)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = AdvertModelSerializer(instance=advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


