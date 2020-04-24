from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLs(db.Model):
    __tablename__ = 'url_list'
    id = db.Column(db.Integer, primary_key=True)
    origial_url = db.Column(db.String(1000))
    short_url = db.Column(db.String(50))
