from authentication.api import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view())
]
