from flask import Flask
from data_manager import DataManager

from models import db, Movie

app = Flask(__name__)

import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'movies.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager() # Create an object of your DataManager class

@app.route('/')
def home():
    return "Welcome to MoviWeb App!"


if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run()