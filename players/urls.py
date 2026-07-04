from django.urls import path
from . import views

urlpatterns = [
    path("", views.players, name="players"),
    path("player/<int:pk>/", views.player_detail, name="player_detail"),
    path("news/", views.news, name="news"),
    path("news/<int:pk>/", views.news_detail, name="news_detail"),
    path("teams/", views.team, name="teams"),
    path("teams/<int:pk>/", views.team_detail, name="team_detail"),
    path("match/", views.match, name="matches"),
    path("match/<int:pk>/", views.match_detail, name="match_detail"),
]