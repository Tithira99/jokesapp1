from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import jokes
from . serializers import jokesSerializer
import random
# Create your views here.

class jokesList(APIView):
    def get(self, request):

        jokes1=list(jokes.objects.all())
        random_items=random.sample(jokes1, 1)
        serializer=jokesSerializer(random_items,many=True)
        return Response(serializer.data)

    def post(self):
        pass