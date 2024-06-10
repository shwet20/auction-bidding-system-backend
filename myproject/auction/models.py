from django.db import models
from core.models import BaseModel
from django.utils import timezone
from users.models import User
from .choices import AuctionStatus

class Auction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='AuctionUser')
    start_time = models.TimeField(default=timezone.now, blank=True, null=True)
    end_time = models.TimeField(default=timezone.now, blank=True, null=True)
    start_price = models.IntegerField(null=True, blank=True)
    item_name = models.CharField(max_length=500)
    auction_status = models.CharField(max_length=50, choices=AuctionStatus.choices, null=True)

    def __str__(self):
        return f"{self.item_name} ({self.start_price})"
    
    # Condition: 
    #  Once the auction is complete, ie crossing end time,  
    #  the auction must be won by the user who has quoted the highest amount
    def complete_auction(self):
        if self.auction_status == AuctionStatus.ACTIVE and self.end_time < timezone.now():
            # Get the highest bid for this auction
            highest_bid = self.bids.order_by('-amount').first()

            if highest_bid:
                self.user = highest_bid.user  # Assign the highest bidder as the winner
                self.auction_status = AuctionStatus.COMPLETED
                self.save()
                return True

        return False