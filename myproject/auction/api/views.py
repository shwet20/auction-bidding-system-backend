# File created at 2024-06-10 17:11:47 UTCfrom rest_framework import viewsets
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from auction import models as models
from auction.api import serializers as serializers
from users.models import Roles
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = models.Auction.objects.all().order_by("start_time", "end_time")
    serializer_class = serializers.AuctionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["auction_status", ]
    http_method_names = ["get", "post", "patch", "delete"]

    # Validations :
    # Normal users must be able to view all auctions that are currently going on
    # Admin should be able to view all the auction status at any time
    
    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        
        if user.role == Roles.ADMIN:
            return queryset
        
        now = timezone.now()
        return queryset.filter(start_time__lte=now, end_time__gte=now)