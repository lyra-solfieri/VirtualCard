
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    linkedin = db.Column(db.String(50), nullable=False)
    github = db.Column(db.String(50), nullable=False)
