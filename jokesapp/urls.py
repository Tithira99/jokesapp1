from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
    path('jokes/', views.jokesList.as_view()),
]