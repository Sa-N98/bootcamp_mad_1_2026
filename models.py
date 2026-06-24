from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class credentials(db.Model):
    __tablename__ = "credentials"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    cretential_type = db.Column(db.String)