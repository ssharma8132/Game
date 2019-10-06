from rest_framework import serializers
from board.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('username','rank','kill','score')


class GameMinimalSerializer(serializers.ModelSerializer):
       class Meta:
            model = Game
            fields = ('match','kill','score')

class GamehyperlinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['match', 'kill', 'score']


