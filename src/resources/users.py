import datetime
from functools import wraps

import jwt
from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from src import db, app
from src.database.models import User
from src.schemas.users import UserSchema


class AutoRegister(Resource):
    user_schema = UserSchema()

    def post(self):
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Such user already exists'}, 409
        return self.user_schema.dump(user), 201


class AuthLogin(Resource):
    def get(self):
        auth = request.authorization
        print(auth)
        if not auth:
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required"}
        user = db.session.query(User).filter_by(username=auth.get('username', '')).first()
        if not user or not check_password_hash(user.password, auth.get('password', '')):
            return "", 401, {"WWW-Authenticate": "Basic realm='Authentication required"}
        token = jwt.encode(
            {
                'user_id': user.id,
                'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
            }, app.config['SECRET_KEY'], algorithm='HS256'
        )
        print(type(token))
        return jsonify(
            {
                "token": token
            }
        )


def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print('in wrapper')
        token = request.headers.get('x-api-key')
        print(token)
        print(type(token))
        if not token:
            return "Not Token", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}
        try:
            user_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
        except (KeyError, jwt.ExpiredSignatureError):
            return "EXCEPT", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}
        user = db.session.query(User).filter_by(id=user_id).first()
        if not user:
            return "Not User", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}
        return func(self, *args, **kwargs)
    return wrapper
