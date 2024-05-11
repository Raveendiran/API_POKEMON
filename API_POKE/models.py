# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PokemonV1Pokemon(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'POKEMON_V1_pokemon'


class PokemonV1User(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    pokemon = models.ForeignKey(PokemonV1Pokemon, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'POKEMON_V1_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EggGroups(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'egg_groups'


class Items(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Locations(models.Model):
    id = models.IntegerField()
    region_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'locations'


class Moves(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(blank=True, null=True)
    contest_type_id = models.IntegerField(blank=True, null=True)
    contest_effect_id = models.IntegerField(blank=True, null=True)
    super_contest_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class Pokemon(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    orderr = models.IntegerField()
    is_default = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonEggGroups(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_egg_groups'


class PokemonFormGenerations(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_generations'


class PokemonMoves(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    orderr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'


class PokemonTypes(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_types'


class Products(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Stats(models.Model):
    id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField()
    is_battle_only = models.SmallIntegerField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class Types(models.Model):
    id = models.IntegerField()
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class Users(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)
    prénom = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    pokemon_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
