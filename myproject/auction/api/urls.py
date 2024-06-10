# File created at 2024-06-10 17:11:47 UTCfrom django.urls import include, path
from rest_framework import routers
from django.urls import path, include
from auction.api import views as auction_views
from users.api import views as user_views

router = routers.DefaultRouter()
router.register(r'auctions', auction_views.AuctionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
