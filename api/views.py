from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import Game
from .serializers import GameSerializer

#Winning combinations
WINNING = [
    [[0, 0], [0, 1], [0, 2]],  # Across top
    [[1, 0], [1, 1], [1, 2]],  # Across middle
    [[2, 0], [2, 1], [2, 2]],  # Across bottom
    [[0, 0], [1, 0], [2, 0]],  # Down left
    [[0, 1], [1, 1], [2, 1]],  # Down middle
    [[0, 2], [1, 2], [2, 2]],  # Down right
    [[0, 0], [1, 1], [2, 2]],  # Diagonal ltr
    [[0, 2], [1, 1], [2, 0]],  # Diagonal rtl
]


@api_view(['POST'])
def create_game(request):
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response("Invalid data type", status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET'])
def get_all_games(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    if serializer.data == []:
        return Response("There are no games", status.HTTP_200_OK)
    else:    
        return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def get_finished_games(request):
    games = Game.objects.filter(is_finished = True)
    serializer = GameSerializer(games, many=True)
    if serializer.data == []:
        return Response("There are no finished games", status.HTTP_200_OK)
    else:    
        return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def get_active_games(request):
    games = Game.objects.filter(is_finished = False)
    serializer = GameSerializer(games, many=True)
    if serializer.data == []:
        return Response("There are no active games", status.HTTP_200_OK)
    else:    
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def get_game(request, pk):
    try:
        game = Game.objects.get(id=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data, status.HTTP_200_OK)
    except:
        return Response("Game with id:{} does not exist".format(pk), status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_game(request, pk):
    try:
        game = Game.objects.get(id=pk)
        game.delete()
        return Response("Game {} deleted succesfully".format(pk), status.HTTP_202_ACCEPTED)
    except:
        return Response("Game with id:{} does not exist".format(pk), status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_game(request, pk):
        try:    
            game = Game.objects.get(id=pk)
            
            data = request.data
            
            #Setting values for validation
            row = data["row"]
            column = data["column"]
            player = data["player"]
            player1 = game.player1[0]
            player2 = game.player2[0]
            s1 = game.player1[1]
            s2 = game.player2[1]

            #Setting values for serializer
            data["player2"] = game.player2
            data["player1"] = game.player1


            #Check that the game is not finished to continue. 
            if game.is_finished and game.winner != None:
                return Response("Game has already finished! the winner is: {}".format(game.winner))
            
            elif game.is_finished and game.winner == None:
                return Response("Game has already finished with a draw")


            #Check that the move is valid
            if player == player1:
                if player == game.next_turn:
                    if (game.board[int(row)][int(column)]) == None:
                        game.board[int(row)][int(column)] = s1
                        data["next_turn"] = player2
                    else:
                        return Response("Invalid board index or already taken space,", status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("It's not {}'s turn".format(player), status.HTTP_400_BAD_REQUEST)
            else: 
                if player == player2:
                    if player == game.next_turn:
                        if (game.board[int(row)][int(column)]) == None:
                            game.board[int(row)][int(column)] = s2
                            data["next_turn"] = player1
                        else:
                            return Response("Invalid board index or already taken space,", status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response("It's not {}'s turn".format(player), status.HTTP_400_BAD_REQUEST)
                else: 
                    return Response("That player is not in this game", status.HTTP_400_BAD_REQUEST)
            
            
            #Check the board for a win 

            board = game.board
            
            for wins in WINNING:
                if board[wins[0][0]][wins [0][1]] == s1 and board[wins[1][0]][wins[1][1]] == s1 and board[wins[2][0]][wins[2][1]] == s1:
                    game.is_finished = True
                    game.winner = player1
                elif board[wins[0][0]][wins [0][1]] == s2 and board[wins[1][0]][wins[1][1]] == s2 and board[wins[2][0]][wins[2][1]] == s2:
                    game.is_finished = True
                    game.winner = player2
                
            
            #Check the board for a draw

            tie_list = []
            for row in board:
                for i in row:
                    tie_list.append(i)

            if None in tie_list:
                pass
            else:
                game.winner = None
                game.is_finished = True


            #Add 1 to movements_played
            game.movements_played += 1
            
            serializer = GameSerializer(instance=game, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response("Invalid data", status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        
        except:
            return Response("Game with id:{} does not exist".format(pk), status.HTTP_400_BAD_REQUEST)



