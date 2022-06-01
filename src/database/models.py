import uuid

from werkzeug.security import generate_password_hash

from src import db

games_companions = db.Table(
    'games_companions',
    db.Column("companion_id", db.Integer, db.ForeignKey('companions.id'), primary_key=True),
    db.Column("game_id", db.Integer, db.ForeignKey('games.id'), primary_key=True)
)


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    developed_by = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Float)
    rating = db.Column(db.Float)
    companions = db.relationship('Companion', secondary=games_companions, lazy='subquery',
                                 backref=db.backref('games', lazy=True))

    def __init__(self, title, release_date, description, developed_by, duration, rating, companions=None):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.developed_by = developed_by
        self.duration = duration
        self.rating = rating
        self.uuid = str(uuid.uuid4())
        if not companions:
            self.companions = []
        else:
            self.companions = companions

    def __repr__(self):
        return f'Game ({self.title}, {self.uuid}, {self.developed_by}, {self.release_date}'


class Companion(db.Model):
    __tablename__ = 'companions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    in_game_class = db.Column(db.String(120), nullable=False)
    debut = db.Column(db.Date, index=True, nullable=False)
    is_romance = db.Column(db.Boolean, index=True)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, name, in_game_class, debut, is_romance):
        self.name = name
        self.in_game_class = in_game_class
        self.debut = debut
        self.is_romance = is_romance
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'Companion ({self.name}, {self.uuid}, {self.in_game_class}, {self.debut}, {self.is_romance})'

    def to_dict(self):
        return {
            'name': self.name,
            'uuid': self.uuid,
            'in-game class': self.in_game_class,
            'debut': self.debut.strftime('%Y-%m-%d'),
            'is romance': self.is_romance
        }


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"User: {self.username}, {self.email}, {self.uuid}"

