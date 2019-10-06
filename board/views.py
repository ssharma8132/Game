from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from board.serializers import *
from board.models import Game


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-score')
    serializer_class = GameSerializer
    # def players(self):
    #     Playerlist = Game.objects.all('-score')[:5]
    #     serializer = GameSerializer(Playerlist,many=True)
    #     return JsonResponse(serializer.data)


class PlayerState(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('match')
    serializer_class = GameMinimalSerializer


class Matchdata(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('match')
    serializer_class = GamehyperlinkSerializer



