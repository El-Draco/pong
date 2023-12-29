from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models import JSONField

# Create your models here.
class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=50, unique=False)
    is_2fa_enabled = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.display_name
    

class User(AbstractUser):
    intra = models.TextField(default="None", primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, unique=False)
    status = models.BooleanField(default=False)
    date_joined = models.DateTimeField() #get current date time
    last_login = models.DateTimeField() #get current date time
    display_name = models.CharField(max_length=50, unique=False)
    def __str__(self):
        return self.intra


class Settings(models.Model):
    avatar = models.TextField(default="None")
    display_name = models.CharField(max_length=50, unique=True, primary_key=True)
    intra = models.ForeignKey(User, on_delete=models.CASCADE)
    is_2fa_enabled = models.BooleanField(default=False)



class Friendship(models.Model):
    intra1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user1')
    intra2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user2')


class Tournament(models.Model):
    intra = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    intra1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='player1')
    intra2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='player2')
    winner = models.CharField(max_length=50)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    

class Nickname(models.Model):
    intra = models.ForeignKey(User, on_delete=models.SET_NULL)
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)