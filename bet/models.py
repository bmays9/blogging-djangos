from django.db import models
import uuid 
from django.contrib.auth.models import User

RESULT = ((0, "Draw"), (1, "Home"), (2, "Away"))
STATUS = ((0, "Pending"), (1, "Win"), (-1, "Lose"))

# Create your models here.
class Bet(models.Model):
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    stake = models.DecimalField(max_digits=10, decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)
    settled = models.IntegerField(choices=STATUS, default=0)
    punter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="placed_by")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    payout =  models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.punter} | {self.id}"



class Line(models.Model):
    home_team = models.CharField(max_length=16)
    away_team = models.CharField(max_length=16)
    prediction = models.IntegerField(choices=RESULT, default=1)
    odds = models.DecimalField(max_digits=10, decimal_places=3)
    match_result = models.IntegerField(choices=STATUS, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    bets = models.ManyToManyField(Bet)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.home_team} v {self.away_team}"

