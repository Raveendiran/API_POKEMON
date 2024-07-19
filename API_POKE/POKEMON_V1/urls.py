from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'user/', views.user),
    path('api/items/<int:item_id>/', views.get_item_by_id),
    path('api/moves/<int:move_id>/<str:move_name>/', views.move),
    path('api/pokemon/<int:pokemon_id>/<str:pokemon_name>/<int:height_value>/<int:weight_value>/<int:exp_value>/', views.get_pokemon_by_id),
    path('/api/connexion/<str:mail>/<str:password>', views.login),
    path('/api/register/<str:mail>/<str:password>', views.register),
    ]