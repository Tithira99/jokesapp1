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

        jokes1=jokes.objects.all()
        serializer=jokesSerializer(jokes1, many=True)
        return Response(serializer.data)

    def post(self):
        pass