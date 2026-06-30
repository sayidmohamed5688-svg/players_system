from django.urls import path
from . import views
urlpatterns = [
    path("",views.players),
    path("player/<int:pk>/",views.player_detail),
    path("news/",views.news),
    path("news/<int:pk>/",views.news_detail)
    
]
