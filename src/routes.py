from src import api
from src.resources.companions import CompanionsListAPI
from src.resources.games import GameListAPI
from src.resources.smoke import Smoke
from src.resources.users import AutoRegister, AuthLogin

api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(GameListAPI, '/games', '/games/<uuid>', strict_slashes=False)
api.add_resource(CompanionsListAPI, '/companions', '/companions/<uuid>', strict_slashes=False)
api.add_resource(AutoRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)
