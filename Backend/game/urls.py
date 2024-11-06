from ninja import NinjaAPI, ModelSchema, Schema
from game.models import Game, Player

api=NinjaAPI()

class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = ["id", "name", "score"]

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = ["id", "name", "turn", "ended"]
    players: list[PlayerSchema]
    
@api.post("/start_game/", response=GameSchema)
def start_game(request, game_id: int):
    return Game.objects.get(pk=game_id)