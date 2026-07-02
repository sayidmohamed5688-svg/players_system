from django.urls import path
from . import views
urlpatterns = [
    path("",views.players),
    path("player/<int:pk>/",views.player_detail),
    path("news/",views.news),
    path("news/<int:pk>/",views.news_detail),
    path("team/", views.team),
    path("team/<int:pk>/", views.team_detail),
    path("matchs/",views.matchs),
    path("match/<int:pk>/", views.match_detail),
    
]
