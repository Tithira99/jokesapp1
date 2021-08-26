from rest_framework import serializers
from . models import jokes

class jokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = jokes
        fields = '__all__'
