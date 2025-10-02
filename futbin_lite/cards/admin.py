from django.contrib import admin
from .models import Player, PlayerCard

# Register your models here.

admin.site.register(Player)


@admin.register(PlayerCard)
class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'position', 'club', 'nation')