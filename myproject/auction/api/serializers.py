# File created at 2024-06-10 17:11:46 UTCfrom rest_framework import serializers
from rest_framework import serializers
from auction.models import Auction
from django.db.models import Q

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}