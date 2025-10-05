from flask import Flask, render_template, url_for, request, redirect
from data_manager import DataManager

from models import db, Movie, User
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'movies.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models
data_manager = DataManager() # Create an object of your DataManager class


@app.route('/')
def home():
    return "Welcome to MoviWeb App!"


@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    try:
        name = request.form.get('name', '').strip()
        if not name:
            return redirect(url_for('index'))

        data_manager.create_user(name)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error in user create_user route call: {e}")
        return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies(user_id):
    """ Show user's favorite movies """
    try:
        user = User.query.get(user_id)
        movies = data_manager.get_movies(user_id)
        return render_template('movies.html', movies=movies, user=user)
    except Exception as e:
        print(f"Error in get_movies route call: {e}")
        return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """ Uses data_manager.add_movie() to fetch movie data """
    try:
        title = request.form.get('name', '').strip()
        if not title:
            return redirect(url_for('get_movies', user_id=user_id))

        #movie =
        data_manager.add_movie(title, user_id)      ############
        # if movie:
        #     data_manager.add_movie(movie)

        return redirect(url_for('get_movies', user_id=user_id))
    except Exception as e:
        print(f"Error in add_movie route: {e}")
        return redirect(url_for('get_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """ Updates a movie's title """
    try:
        new_title = request.form.get('new_title', '').strip()
        if not new_title:
            return redirect(url_for('get_movies', user_id=user_id))

        data_manager.update_movie(movie_id, user_id, new_title)
        return redirect(url_for('get_movies', user_id=user_id))

    except Exception as e:
        print(f"Unexpected error in update_movie: {e}")
        return redirect(url_for('get_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """ Deletes movie """
    data_manager.delete_movie(movie_id, user_id)
    return redirect(url_for('get_movies', user_id=user_id))

# Handles 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('Err404.html'), 404 #########


if __name__ == '__main__':
  # with app.app_context():
  #   db.create_all()
    app.run(debug=True)