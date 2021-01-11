from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieDataSerializer
from .models import MovieData


# Create your views here.

class MovieSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionMovieSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='Action')
    serializer_class = MovieDataSerializer


class ComedyMovieSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='Comedy')
    serializer_class = MovieDataSerializer


class DramMovieSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='Dram')
    serializer_class = MovieDataSerializer
