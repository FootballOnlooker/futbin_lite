from django.shortcuts import render, get_object_or_404
from .models import PlayerCard


# Create your views here.
def player_list(request):
    players = PlayerCard.objects.all()
    return render(request, 'cards/player_list.html', {'players': players})


def player_detail(request, pk):
    player = get_object_or_404(PlayerCard, pk=pk)
    return render(request, 'cards/player_detail.html', {'player': player})
