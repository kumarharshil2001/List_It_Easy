from django.contrib import admin
from .models import User, Listing, Bid,Comment,Watchlist,Closedbid,allitems

# Register your models here.
admin.site.register(User)
admin.site.register(allitems)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Closedbid)
admin.site.register(Watchlist)
admin.site.register(Comment)