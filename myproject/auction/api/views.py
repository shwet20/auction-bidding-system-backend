from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from auction.models import Auction, Bid
from auction.api.serializers import AuctionSerializer, BidSerializer
from users.models import Roles
from django_filters.rest_framework import DjangoFilterBackend

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all().order_by("start_time", "end_time")
    serializer_class = AuctionSerializer
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

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
