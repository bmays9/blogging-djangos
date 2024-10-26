from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Bet, Line

# Create your views here.
class OpenBets(generic.ListView):
    """
    Renders the bets page
    """           
    queryset = Bet.objects.filter(settled='0')
    template_name = "bet/bets.html"
    paginate_by = 5