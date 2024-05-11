from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

def welcome (requests):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def details_user (requests):
    user = Users.objects.get(nom='RAVEE')
    message = "le nom d'utilisateur est {} et son prenom {}".format(user.nom, user.prenom)
    return JsonResponse({"message":message})

def get_item (requests, item_id):
    id = int(item_id)
    item = Items.objects.get(id = id)
    if resquests.method == 'GET':
        message = "Item correspod à l'id {} est {}".format(id,item.identifier)
        return JsonResponse({"message":message})
    if resquests.method == 'DELETE': 
        Items.objects.delete(id = id)
        return HttpResponse("Item {} dont id est {}, est supprimer de votre base".format(id, item.identifier))

@csrf_exempt
def get_move(request, move_id, move_name):
    if request.method == 'GET':
        try:
            move = Moves.objects.get(id=move_id)
            move_data = {
                "id": move.id,
                "name": move.identifier,
            }
            return JsonResponse(move_data)
        except Moves.DoesNotExist:
            return JsonResponse({"error": "Move pas trouvé"}, status=404)
    elif request.method == 'PUT':
        try:
            move = Moves.objects.get(id=move_id)
            move.identifier = move_name
            move.save()
            return JsonResponse({"message": "Move est mis a jour avec succès", "id": move.id})
        except Moves.DoesNotExist:
            return JsonResponse({"error": "Move pas trouvé"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "GET et PUT requests sont autorisées"}, status=405)


@csrf_exempt
def get_pokemon_by_id(request, pokemon_id, pokemon_name, height_value, weight_value, exp_value):
    id = int(pokemon_id)
    if request.method == 'GET':
        try:
            pokemon = Pokemon.objects.get(id=id)
            message = "Le Pokemon correspondant a l'ID {} est {}".format(id, pokemon.identifier)
            return JsonResponse({"message": message})
        except Pokemon.DoesNotExist:
            return JsonResponse({"error": "Pokemon non trouve"}, status=404)
    elif request.method == 'POST':
        try:
            max_id = Pokemon.objects.latest('id').id + 1
        except Pokemon.DoesNotExist:
            max_id = 0
        try:
            new_pokemon = Pokemon.objects.create(id = max_id, identifier=pokemon_name, height=height_value, weight=weight_value, base_experience=exp_value, orderr = 5, is_default = 3)
            return JsonResponse({"message": "Le Pokemon a ete cree avec succes", "id": new_pokemon.id, "name": new_pokemon.identifier})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Seules les requetes GET et POST sont autorisees"}, status=405)



def connexion(request, mail, password):
    if request.method == 'POST':
        user = authenticate(request, username=mail, password=password)
        if user is not None:
            return JsonResponse({"message": "Connexion réussie"})
        else:
            return JsonResponse({"error": "Nom d'utilisateur ou mot de passe incorrect"}, status=400)
    else:
        return JsonResponse({"error": "Seules les requêtes POST sont autorisées"}, status=405)


def register(request,mail,password):
    if request.method == 'POST':
        if User.objects.filter(username=mail).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        
        return JsonResponse({"message": "User registered successfully"})

    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
