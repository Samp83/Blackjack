from ninja import NinjaAPI, ModelSchema, Schema
from game.models import Game, Player
from django.db import IntegrityError

api = NinjaAPI()

class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = ["id", "name", "score"]

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = ["id", "name", "turn", "ended"]
    players: list[PlayerSchema]

class StartGameRequest(Schema):
    game_name: str
    players: list[str]

class AddPlayersRequest(Schema):
    players: list[str]

class UpdateScoreRequest(Schema):
    score: int

class ConfirmWipeRequest(Schema):
    confirm: bool

@api.post("/start_game/", response=GameSchema)
def start_game(request, data: StartGameRequest):
    game = Game.objects.create(name=data.game_name)
    
    for name in data.players:
        Player.objects.create(name=name, game=game)
    
    game.refresh_from_db()
    return game

@api.post("/add_players/{game_id}/", response=GameSchema)
def add_players(request, game_id: int, data: AddPlayersRequest):
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return {"error": "Game not found"}, 404

    for name in data.players:
        Player.objects.create(name=name, game=game)

    game.refresh_from_db()
    return game

@api.put("/update_score/{player_id}/", response=PlayerSchema)
def update_score(request, player_id: int, data: UpdateScoreRequest):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return {"error": "Player not found"}, 404

    player.score = data.score
    player.save()
    return player

@api.delete("/wipe_database/")
def wipe_database(request, data: ConfirmWipeRequest):
    if data.confirm:
        Game.objects.all().delete()
        Player.objects.all().delete()
        return {"message": "Database wiped successfully"}
    else:
        return {"error": "Confirmation required"}, 400

@api.get("/get_game/{game_id}/", response=GameSchema)
def get_game(request, game_id: int):
    try:
        game = Game.objects.prefetch_related("players").get(id=game_id)
    except Game.DoesNotExist:
        return {"error": "Game not found"}, 404

    return game

@api.get("/get_player/{player_id}/", response=PlayerSchema)
def get_player(request, player_id: int):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return {"error": "Player not found"}, 404

    return player
