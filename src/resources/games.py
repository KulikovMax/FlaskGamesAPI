from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Game
# from src.resources.users import token_required
from src.schemas.games import GameSchema


class GameListAPI(Resource):
    game_schema = GameSchema()

    # @token_required
    def get(self, uuid=None):
        if not uuid:
            games = db.session.query(Game).all()
            return self.game_schema.dump(games, many=True), 200
        game = db.session.query(Game).filter_by(uuid=uuid).first()
        if not game:
            return '', 404
        return self.game_schema.dump(game), 200

    def post(self):
        try:
            game = self.game_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(game)
        db.session.commit()
        return self.game_schema.dump(game), 201

    def put(self, uuid):
        game = db.session.query(Game).filter_by(uuid=uuid).first()
        if not game:
            return "", 404
        try:
            game = self.game_schema.load(request.json, instance=game, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(game)
        db.session.commit()
        return self.game_schema.dump(game), 200

    def patch(self, uuid):
        game = db.session.query(Game).filter_by(uuid=uuid).first()
        if not game:
            return '', 404
        game_json = request.json
        for key, value in game_json.items():
            if key == 'release_date':
                value = datetime.strptime(value, '%B %d, %Y')
            setattr(game, key, value)
        db.session.add(game)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        game = db.session.query(Game).filter_by(uuid=uuid).first()
        if not game:
            return '', 404
        db.session.delete(game)
        db.session.commit()
        return '', 204
