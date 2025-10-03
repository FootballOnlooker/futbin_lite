from django.shortcuts import render
from .models import PlayerCard


# Create your views here.
def player_list(request):
    players = PlayerCard.objects.all()
    return render(request, 'cards/player_list.html', {'players': players})
