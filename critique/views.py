from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Review

class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer