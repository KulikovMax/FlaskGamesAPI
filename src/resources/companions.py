from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Companion
from src.schemas.companions import CompanionSchema


class CompanionsListAPI(Resource):
    companion_schema = CompanionSchema()

    def get(self, uuid=None):
        if not uuid:
            companions = db.session.query(Companion).all()
            return self.companion_schema.dump(companions, many=True), 200
        companion = db.session.query(Companion).filter_by(uuid=uuid).first()
        if not companion:
            return '', 404
        return self.companion_schema.dump(companion), 200

    def post(self):
        try:
            companion = self.companion_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(companion)
        db.session.commit()
        return self.companion_schema.dump(companion), 201

    def put(self, uuid):
        companion = db.session.query(Companion).filter_by(uuid=uuid).first()
        if not companion:
            return "", 404
        try:
            companion = self.companion_schema.load(request.json, instance=companion, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(companion)
        db.session.commit()
        return self.companion_schema.dump(companion), 200

    def patch(self, uuid):
        companion = db.session.query(Companion).filter_by(uuid=uuid).first()
        if not companion:
            return '', 404

        game_json = request.json
        for key, value in game_json.items():
            if key == 'release_date':
                value = datetime.strptime(value, '%B %d, %Y')
            setattr(companion, key, value)
        db.session.add(companion)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        companion = db.session.query(Companion).filter_by(uuid=uuid).first()
        if not companion:
            return '', 404
        db.session.delete(companion)
        db.session.commit()
        return '', 204
