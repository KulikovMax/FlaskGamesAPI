from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Game


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        exclude = ['id']
        load_instance = True
        include_fk = True

    companions = Nested('CompanionSchema', many=True, exclude=('games',))
