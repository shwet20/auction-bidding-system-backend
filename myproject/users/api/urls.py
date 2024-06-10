from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
