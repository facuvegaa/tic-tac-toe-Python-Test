from django.urls import path

from . import views

urlpatterns = [
    path('create_game/', views.create_game, name="create_game"),
    path('get_all_games/', views.get_all_games, name="get_all_games"),
    path('get_finished_games/', views.get_finished_games, name="get_finished_games"),
    path('get_active_games/', views.get_active_games, name="get_active_games"),
    path('update_game/<str:pk>/', views.update_game, name="update_game"),
    path('delete_game/<str:pk>/', views.delete_game, name="delete_game"),
    path('get_game/<str:pk>/', views.get_game, name="get_game")
]