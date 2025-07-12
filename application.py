import os
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    jsonify,
)
import requests
from database import app, db, Book, User, Review

API_KEY = os.getenv("API_KEY")
API_URL = "https://www.googleapis.com/books/v1/volumes"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session["user_id"] = user.id
            flash("Login successful", "success")
            return redirect(url_for("search"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")


@app.route("/search")
def search():
    user_id = session.get("user_id")
    print(user_id)
    return render_template("search.html")


@app.route("/search-books", methods=["POST"])
def search_books():
    search_term = (
        request.form.get("isbn")
        or request.form.get("title")
        or request.form.get("author")
    )
    if not search_term:
        return render_template(
            "search.html", error="Please enter a search term."
        )
    if request.form.get("isbn"):
        search_parameter = f"isbn:{search_term}"
    elif request.form.get("title"):
        search_parameter = f"title:{search_term}"
    else:
        search_parameter = f"inauthor:{search_term}"
    url = f"{API_URL}?q={search_parameter}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            books = []
            for item in data["items"]:
                title = item["volumeInfo"]["title"]
                authors = item["volumeInfo"].get("authors", [])
                book_id = item["id"]
                isbn = (
                    item["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                    if "industryIdentifiers" in item["volumeInfo"]
                    else "Not available"
                )
                images = (
                    item["volumeInfo"].get("imageLinks", {}).get("thumbnail", "")
                )
                book_info = {
                    "title": title,
                    "authors": ", ".join(authors) if authors else "Unknown",
                    "isbn": isbn,
                    "id": book_id,
                    "images": images,
                }
                books.append(book_info)
            return render_template("search.html", books=books)
        else:
            return render_template(
                "search.html",
                error="No books found matching your search.",
            )
    else:
        return render_template(
            "search.html", error="Could not retrieve book information."
        )


@app.route("/book/<id>")
def book_detail(id):
    url = f"{API_URL}/{id}?key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "volumeInfo" in data:
            book = data["volumeInfo"]
            reviews = Review.query.filter_by(book_id=id).all()
            return render_template(
                "book_detail.html", book=book, book_id=id, reviews=reviews
            )
        else:
            return render_template(
                "book_detail.html", error="Book not found."
            )
    else:
        return render_template(
            "book_detail.html", error="Could not retrieve book information."
        )


@app.route("/write-review", methods=["POST"])
def write_review():
    if "user_id" not in session:
        flash("You must be logged in to write a review.", "danger")
        return redirect("/")
    user_id = session["user_id"]
    book_id = request.form.get("book_id")
    rating = request.form.get("rating")
    text = request.form.get("text")
    user = User.query.get(user_id)
    if user:
        username = user.username
    else:
        username = "Unknown user"
    existing_review = Review.query.filter_by(user_id=user_id, book_id=book_id).first()
    if existing_review:
        flash("You have already written a review for this book.", "danger")
    else:
        new_review = Review(
            user_id=user_id,
            book_id=book_id,
            rating=rating,
            text=text,
            username=username,
        )
        db.session.add(new_review)
        db.session.commit()
        flash("Review submitted successfully.", "success")
    return redirect(f"/book/{book_id}")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logout successful", "success")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if not username or not password or not confirm_password:
            flash("Please complete all fields.", "danger")
        else:
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                flash(
                    "Username already exists. Please choose another.", "danger"
                )
            elif password != confirm_password:
                flash(
                    "Passwords do not match. Please try again.",
                    "danger",
                )
            else:
                new_user = User(username=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                session["user_id"] = new_user.id
                flash("Registration successful. You can now log in.", "success")
                return redirect(url_for("search"))
    return render_template("register.html")


@app.route("/api/<isbn>")
def book_api(isbn):
    query = db.session.query(Book).filter_by(isbn=isbn)
    book = query.first()
    if book:
        book_data = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "year": book.year,
        }
        url = f"{API_URL}?q=isbn:{isbn}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                item = data["items"][0]
                volume_info = item.get("volumeInfo", {})
                book_data["ratingsCount"] = volume_info.get(
                    "ratingsCount", "Not available"
                )
                book_data["averageRating"] = volume_info.get(
                    "averageRating", "Not available"
                )
        return jsonify(book_data)
    else:
        return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
