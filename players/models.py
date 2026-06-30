from django.db import models
class Player(models.Model):
    name=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    xaafadd=models.CharField(max_length=100)
    age=models.IntegerField()
    bio=models.TextField()
    
    def __str__(self):
        return self.name
    
class team(models.Model):
    name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    logo=models.URLField()
    founded=models.IntegerField()

    def __str__(self):
        return self.name
    

class News(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.URLField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Match(models.Model):
    home_team=models.CharField(max_length=100)
    away_team=models.CharField(max_length=100)
    home_team_score=models.IntegerField()
    away_team_score=models.IntegerField()
    date=models.DateField()
    stadium=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
