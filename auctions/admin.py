from django.contrib import admin

# Register your models here.

from .models import CreateListing, Comment, Bid, Tag, Watchlist

admin.site.register(Comment)
admin.site.register(CreateListing)
admin.site.register(Bid)
admin.site.register(Tag)
admin.site.register(Watchlist)
