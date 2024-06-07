from django.urls import path, include
from .views import ReviewViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'review', ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
    
]