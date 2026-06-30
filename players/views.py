from django.shortcuts import render
from .models import Player , News
def players(request):
    all_players=Player.objects.all()
    return render(request ,"players/players.html", {"players": all_players})
# Create your views here.
def player_detail(request):
    player=player.objects.get(id=pk)
    return render (request,"players/player_detail.html",{"player": player})

def news(request):
    all_news=News.objects.all()
    return render (request, "players/news.html", {"news": all_news})

def news_detail(request , id):
    article=News.objects.get(id=pk)
    return render (request , "players/news_detail.html", {"article": article} )
