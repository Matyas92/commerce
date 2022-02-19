from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("entry/<str:pk>", views.entry, name="entry"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("createWatchlist/<event_id>", views.createWatchlist, name="createWatchlist"),

    path("categories", views.categories, name="categories"),
    path("delete_event/<event_id>", views.delete_event, name="delete-event"),
    path("add_event/<event_id>", views.add_event, name="add-event"),

    path("bidTo/<str:pk>", views.bidTo, name="bid-to"),
    path("closebid/<str:pk>", views.closeBid, name="closeBid"),

    #path("create_bid/<str:pk>", views.create_bid, name="createBid")


]
