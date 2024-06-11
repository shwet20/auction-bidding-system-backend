from rest_framework import serializers
from auction.models import Auction, Bid

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'auction', 'user', 'amount', 'timestamp']
        extra_kwargs = {'user': {'read_only': True}}

    def validate(self, data):
        auction = data['auction']
        if auction.end_time < timezone.now():
            raise serializers.ValidationError("Cannot place a bid on an auction that has ended.")
        return data

class AuctionSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)

    class Meta:
        model = Auction
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
