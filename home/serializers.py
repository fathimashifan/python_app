from rest_framework import serializers
from .models import MovieDisplay

class MovieDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDisplay
        fields = '__all__'
