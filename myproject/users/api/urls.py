from django.urls import path
from users.api import views


urlpatterns = [
    path('', views.UserGetUpdateView.as_view())
]
