from database import app, db

with app.app_context():
    db.drop_all()
    print("¡Todas las tablas han sido eliminadas!") 