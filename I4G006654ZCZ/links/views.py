from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Link

from .serializers import LinkSerializer


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

# Create your views here.
