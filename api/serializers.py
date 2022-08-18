from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
    
    # When creating an instance, it checks that the user has chosen a symbol to play, 
    # if not, X is automatically set for player1 and O for player2.
    # It also validates that the next turn is for an existing player.
    def create(self, validated_data):
        game = Game()
        game.player1 = validated_data["player1"]
        game.player2 = validated_data["player2"]
        game.next_turn = validated_data["next_turn"]
        print(game.next_turn)
        if len(game.player1) == 1:
            game.player1.append("X")
        if len(game.player2) == 1:
            game.player2.append("O")
        if game.next_turn != game.player1[0] and game.next_turn != game.player2[0]:
            error = 'Next turn must be a player'
            raise serializers.ValidationError(error)
        return Game.objects.create(**validated_data)

    