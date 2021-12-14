from .models import MovieDetails
from rest_framework import serializers

class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetails
        fields = '__all__'