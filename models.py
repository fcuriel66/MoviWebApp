from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import backref

db = SQLAlchemy()   # Define db as SQLAlchemy


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    # Equivalent to one-to-many SQL relationship
    #movies = db.relationship('Movie', backref='user', lazy=True)   To try if  for key below fails

    def __repr__(self):
        return f'User= {self.name}, ID= {self.id}'


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(300))
    # Foreign key - users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # "SQL" type of relationship to users
    user = db.relationship('User', backref=db.backref('movies', lazy=True))

    def __repr__(self):
        return f"<Movie {self.id}: {self.name}>"

    def __str__(self):
        return f"Movie {self.name} released the year {self.year} "