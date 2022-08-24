from turtle import update
from urllib import response
from venv import create
from rest_framework.test import APITestCase
from rest_framework import status
from api import serializers

from api.serializers import GameSerializer

from .models import Game

class CreateGameTestCase(APITestCase):
    
    def test_create_game(self):
        data={"player1": ["test1"], "player2":["test2"], "next_turn":"test1"}
        response = self.client.post("/api/create_game/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetGamesTestCase(APITestCase):

    def test_get_all_games(self):
        response = self.client.get("/api/get_all_games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_finished_games(self):
        response = self.client.get("/api/get_finished_games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_active_games(self):
        response = self.client.get("/api/get_active_games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

class RetriveGameTestCase(APITestCase):

    def test_retrive_game(self):
        game = Game.objects.create(player1=["test1", "X"], player2=["test2", "O"], next_turn="test1")
        data={"player1": ["test1"], "player2":["test2"], "next_turn":"test1"}
        serializer = GameSerializer(instance=game, data=data)
        serializer.is_valid()
        serializer.save()
        response = self.client.get("/api/get_game/{}/".format(game.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

class DeleteGameTestCase(APITestCase):

    def test_delete_game(self):
        game = Game.objects.create(player1=["test1", "X"], player2=["test2", "O"], next_turn="test1")
        data={"player1": ["test1"], "player2":["test2"], "next_turn":"test1"}
        serializer = GameSerializer(instance=game, data=data)
        serializer.is_valid()
        serializer.save()
        response = self.client.delete("/api/delete_game/{}/".format(game.id))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

class UpdateGameTestCase(APITestCase):

    def test_update_game(self):
        game = Game.objects.create(player1=["test1", "X"], player2=["test2", "O"], next_turn="test1")
        data_game={"player1": ["test1", "X"], "player2":["test2", "O"], "next_turn":"test1"}
        serializer = GameSerializer(instance=game, data=data_game)
        serializer.is_valid()
        serializer.save()
        data={"player":"test1", "row":"0" , "column":"0"}

        response = self.client.post("/api/update_game/{}/".format(game.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)