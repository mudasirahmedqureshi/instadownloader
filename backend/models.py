from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Download(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
