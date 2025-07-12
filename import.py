import csv
from database import app, db, Book

with app.app_context():
    db.create_all()
    if not db.session.query(Book.query.exists()).scalar():
        with open("books.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                book = Book(
                    isbn=row["isbn"],
                    title=row["title"],
                    author=row["author"],
                    year=int(row["year"]),
                )
                db.session.add(book)
        db.session.commit()
        print("Data uploaded successfully")
    else:
        print("Database has already been loaded")