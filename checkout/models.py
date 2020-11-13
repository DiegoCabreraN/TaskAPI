from app import db


class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(200), unique=False, nullable=False)
    country = db.Column(db.String(128), unique=False, nullable=False)
    lastNums = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    itemList = db.Column(db.String(512), unique=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.id)

    def as_dict(self):
        return {
            'id': int(self.id),
            'username': str(self.username),
            'address': str(self.address),
            'country': str(self.country),
            'lastNums': int(self.lastNums),
            'total': int(self.total),
            'itemList': self.itemList,
        }
