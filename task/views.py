from django.db.models import manager
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieDetailsSerializer
from .models import MovieDetails
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET'])
def home(request):
    movie_datails = MovieDetails.objects.all()
    serializer = MovieDetailsSerializer(movie_datails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, slug):
    movie_datails = MovieDetails.objects.get(slug=slug)
    serializer = MovieDetailsSerializer(movie_datails, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def movie_create(request):
    serializer = MovieDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)