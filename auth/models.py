from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.id)
