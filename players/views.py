from django.shortcuts import render
from .models import Player , News , Team , Match
def players(request):
    all_players=Player.objects.all()
    return render(request ,"players/players.html", {"players": all_players})
# Create your views here.
def player_detail(request , pk):
    player=Player.objects.get(id=pk)
    return render (request,"players/player_detail.html",{"player": player})

def news(request):
    all_news=News.objects.all()
    return render (request, "players/news.html", {"news": all_news})

def news_detail(request , pk):
    article=News.objects.get(id=pk)
    return render (request , "players/news_detail.html", {"article": article} )

def team(request):
    all_teams=Team.objects.all()
    return render (request , "players/teams.html", {"teams": all_teams})

def team_detail(request , pk):
    team=Team.objects.get(id=pk)
    return render (request , "players/team_detail.html", {"team": team })

def match(request):
    all_matchs=Match.objects.all()
    return render(request,"players/matches.html", {"matches": all_matchs})

def match_detail(request , pk):
    match=Match.objects.get(id=pk)
    return render(request , "players/match_detail.html", {"match": match})
