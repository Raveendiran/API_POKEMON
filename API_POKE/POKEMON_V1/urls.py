from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'', views.welcome),
    path(r'user/', views.details_user),
    path('api/items/<int:item_id>/', views.get_item),
    path('api/moves/<int:move_id>/<str:move_name>/', views.get_move),
    path('api/pokemon/<int:pokemon_id>/<str:pokemon_name>/<int:height_value>/<int:weight_value>/<int:exp_value>/', views.get_pokemon_by_id),
    path('/api/connexion/<str:mail>/<str:password>', views.connexion),
    path('/api/register/<str:mail>/<str:password>', views.register),
    #path('api/pokemon/<str:type>/', views.identifier_pokemon),
    #path('api/pokemon/<str:pokemon_name>/', views.get_pokemon_by_name),
    #path('api/pokemon/types/<str:pokemon_type>/', views.get_pokemon_by_type),
    #re_path(r'(?P<album_id>[0-9]+)/', views.details),
    #path(r'search/', views.search),
    ]