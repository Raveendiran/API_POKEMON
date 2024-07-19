from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
def user(requests):
    user = Users.objects.get(nom='ANNE')
    message = "User name is {} and first name is {}".format(user.nom, user.prenom)
    return JsonResponse({"message": message})
 
def get_item_by_id(requests, item_id):
    id = int(item_id)
    item = Items.objects.get(id=id)
    print(HttpResponse("{}".format(requests.method)))
    if requests.method == 'GET':
        message = "Item corresponding to id {} is {}".format(id, item.identifier)
        return JsonResponse({"message": message})
 
@csrf_exempt
def move(request, move_id, move_name):
    if request.method == 'GET':
        try:
            move = Moves.objects.get(id=move_id)
            move_data = {
                "id": move.id,
                "name": move.identifier,
            }
            return JsonResponse(move_data)
        except Moves.DoesNotExist:
            return JsonResponse({"error": "Move not found"}, status=404)
    elif request.method == 'PUT':
        try:
            move = Moves.objects.get(id=move_id)
            move.identifier = move_name
            move.save()
            return JsonResponse({"message": "Move updated successfully", "id": move.id})
        except Moves.DoesNotExist:
            return JsonResponse({"error": "Move not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only GET and PUT requests are allowed"}, status=405)
 
@csrf_exempt
def get_pokemon_by_id(request, pokemon_id, pokemon_name, height_value, weight_value, exp_value):
    id = int(pokemon_id)
    if request.method == 'GET':
        try:
            pokemon = Pokemon.objects.get(id=id)
            message = "The Pokemon corresponding to ID {} is {}".format(id, pokemon.identifier)
            return JsonResponse({"message": message})
        except Pokemon.DoesNotExist:
            return JsonResponse({"error": "Pokemon not found"}, status=404)
    elif request.method == 'POST':
        try:
            max_id = Pokemon.objects.latest('id').id + 1
        except Pokemon.DoesNotExist:
            max_id = 0
        try:
            new_pokemon = Pokemon.objects.create(id=max_id, identifier=pokemon_name, height=height_value, weight=weight_value, base_experience=exp_value, orderr=5, is_default=3)
            return JsonResponse({"message": "The Pokemon was created successfully", "id": new_pokemon.id, "name": new_pokemon.identifier})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only GET and POST requests are allowed"}, status=405)
 
def login(request, mail, password):
    if request.method == 'POST':
        user = authenticate(request, username=mail, password=password)
        if user is not None:
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
    

def register(request, mail, password):
    if request.method == 'POST':
        if User.objects.filter(username=mail).exists():
            return JsonResponse({"error": "User already exists"}, status=400)
 
        user = User.objects.create_user(username=mail, password=password)
        return JsonResponse({"message": "User registered successfully"})
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)