from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("submit",views.submit,name="submit"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("listings/<int:id>",views.listingpage,name="listingpage"),
    path("submitbid/<int:listingid>",views.submitbid,name="submitbid"),
    path("closebid/<int:listingid>",views.closebid,name="closebid"),
    path("commentsubmit/<int:listingid>",views.commentsubmit,name="commentsubmit"),
    path("watchlist/<str:username>",views.watchlistpage,name="watchlistpage"),
    path("addwatchlist/<int:listingid>",views.addwatchlist,name="addwatchlist"),
    path("removewatchlist/<int:listingid>",views.removewatchlist,name="removewatchlist"),
    path("mywinnings",views.mywinnings,name="mywinnings")
]