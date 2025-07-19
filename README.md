# Project 1 - Web Library 📚

Web Programming with Python and JavaScript

**Project deployed on Render! 🚀**

Access it here: [https://cs50w-books.onrender.com/](https://cs50w-books.onrender.com/)

## Inspiration and Differences 💡

This project is inspired by [CS50W Project 1](https://docs.cs50.net/ocw/web/projects/1/project1.html).

**Main differences:**

* The original project requires using Heroku for the database and the Goodreads API for external ratings.
* This version uses Render.com for the database and the Google Books API, because **an earlier version of the original project required exactly those services** (Render and Google Books). Therefore, the differences are minimal and only affect minor integration and presentation details.

---

## Description 📝

This project is a web application for searching books, viewing details, posting reviews, and managing users. It uses Flask, SQLAlchemy, and the Google Books API. You can use a PostgreSQL database (recommended for production) or SQLite (easier for local testing).

---

## Screenshots 📸

Below are some screenshots of the application in different views and modes:

* **Search screen (light mode):**
  ![Search screen light mode](static/images/search_light.png)

* **Search screen (dark mode):**
  ![Search screen dark mode](static/images/search_black.png)

* **Login screen (light mode):**
  ![Login screen light mode](static/images/login.png)

* **Login screen (dark mode):**
  ![Login screen dark mode](static/images/login_black.png)

* **Registration screen:**
  ![Registration screen](static/images/register.png)

---

## Project Structure 🗂️

* `application.py`: Main Flask application logic
* `database.py`: Database models and configuration
* `import.py`: Script to import books from CSV (must be run manually to load initial data)
* `drop_all.py`: Script to drop all tables
* `static/`: Static assets (CSS, images, JS)
* `templates/`: Jinja2 HTML templates
* `books.csv`: Sample book data
* `requirements.txt`: Project dependencies

---

## Prerequisites ⚙️

* Python 3.x
* pip
* (Optional) An account on [Render.com](https://render.com/) for a free PostgreSQL database

---

## 1. Create and activate a virtual environment 🐍

```powershell
python -m venv myenv
myenv\Scripts\activate
```

---

## 2. Install dependencies 📦

```powershell
pip install -r requirements.txt
pip install flask_wtf
```

---

## 3. Configure environment variables 🔑

### Option A: Use SQLite (easier for local testing)

No need to set `DATABASE_URL`. The project can be configured to use SQLite by editing `application.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
```

### Option B: Use PostgreSQL on Render.com

1. Create an account at [Render.com](https://render.com/)
2. Go to "Dashboard" > "New" > "PostgreSQL"
3. Name your database and create the service
4. Copy the connection URL (format: `postgresql://user:password@host:port/dbname`)
5. In your terminal, set the environment variable:

```powershell
$env:DATABASE_URL = "<your_connection_url>"
```

---

## 4. Other required environment variables 🧩

```powershell
$env:API_KEY = "<your_google_books_api_key>"
$env:FLASK_APP = "application.py"
$env:SECRETKEY = "secretkey"
$env:FLASK_DEBUG = 1
```

---

## 5. Run the application ▶️

```powershell
flask run
```

Or:

```powershell
python application.py
```

---

## 6. First-time setup 🚦

* If the database is empty, **you must manually run** the `import.py` script to load data from `books.csv`:

```powershell
python import.py
```

* You can register a new account through the web interface.
* Searches can be performed by ISBN, title, or author.
* Only one review is allowed per book and it cannot be edited.
