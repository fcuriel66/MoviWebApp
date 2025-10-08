# MoviWebApp

MoviWebApp is a web application built with Flask that allows users to manage movie collections. Users can be created, movies can be added, updated, and deleted, and each user has their own movie list. The app uses SQLite files for data persistence and supports a clean UI layout. Movie metadata fetched from OMDb API.

---

## 🚀 Features

- User management: create, view, delete users  
- Movie management per user: add, update, delete movies  
- Responsive gallery-style layout for movie posters
- Fetching of rellable movie metadata though OMDb API
- SQLite-based storage (SQL database)  
- Clean, modern UI with fixed header/footer and scrolling movie carousel  
- Separation between templates and static assets

---

## 📁 Project Structure
```
MoviWebApp/

├── app.py 
├── models.p 
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── movies.html
│ └── ...
├── static/
│ └── style.css
├── data/
│ └── movies.db
├── requirements.txt
└── README.md
```

- `app.py` — main Flask application: routes, logic
- data_manager.py - Add, get, update and delete management of tables  
- `models.py` — data models for User/Movie  
- `templates/` — Jinja2 templates for HTML pages  
- `static/` — CSS, images, and other static files  
- `data/` — SQLite files storing users and movies (movies.db)  
- `requirements.txt` — Python dependencies

---

## 🧰 Setup & Installation

### Prerequisites

- Python 3.8+  
- pip  

### Steps

1. Clone the repository:

   ```bash
   git clone git@github.com:fcuriel66/MoviWebApp.git
   cd MoviWebApp
### Usage and Routes
   
| Route                                       | Methods    | Purpose                            |
| ------------------------------------------- | ---------- | ---------------------------------- |
| `/`                                         | GET        | Landing or redirect to user list   |
| `/users`                                    | GET        | Show all users                     |
| `/users/new`                                | GET / POST | Form to add a new user             |
| `/users/<user_id>/movies`                   | GET        | Display that user’s movie gallery  |
| `/users/<user_id>/movies/add`               | GET / POST | Add a new movie for user           |
| `/users/<user_id>/movies/<movie_id>/update` | GET / POST | Update movie title                 |
| `/users/<user_id>/movies/<movie_id>/delete` | POST       | Delete a movie                     |
| `/users/<user_id>/delete`                   | POST       | Delete a user and all their movies |
