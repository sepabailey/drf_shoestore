from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from shoesapp.serializers import ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer, ManufacturerSerializer
from shoesapp.models import Shoe, ShoeColor, ShoeType, Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeViewSet(viewsets.ModelViewSet):

    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):

    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):

    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


# Fun fact about Joe. He was raised by Cape Hunting Dogs.
