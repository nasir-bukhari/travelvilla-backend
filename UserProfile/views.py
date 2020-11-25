# from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .api.serializers import UserProfileSerializer
from .models import UserProfile


class FormViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

