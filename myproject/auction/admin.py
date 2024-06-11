from django.contrib import admin
from core.admin import get_model_fields
from auction.models import Auction, Bid

# Register your models here.
class AuctionsAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Auction)
    ordering = ("item_name",)
    list_filter = ("auction_status", "user", )

class BidAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Bid)
    ordering = ("user", "auction", )
    list_filter = ("auction", )

admin.site.register(Auction, AuctionsAdmin)
admin.site.register(Bid, BidAdmin)