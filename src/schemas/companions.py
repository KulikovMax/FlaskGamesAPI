from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Companion


class CompanionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Companion
        exclude = ['id']
        load_instance = True
        include_fk = True

    games = Nested('GameSchema', many=True, exclude=('companions',))
