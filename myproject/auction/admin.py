from django.contrib import admin
from core.admin import get_model_fields
from auction.models import Auction

# Register your models here.
class AuctionsAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Auction)
    ordering = ("item_name",)
    list_filter = ("auction_status", "user", )

admin.site.register(Auction, AuctionsAdmin)