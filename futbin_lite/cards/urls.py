from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path("players/", views.player_list, name="player_list"),
    path('players/<int:pk>/', views.player_detail, name="player_detail")
]
