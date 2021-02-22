from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, unique=False, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, default=False,  nullable=False)

    def __repr__(self):
        return '<Task {}>'.format(self.title)

    def as_dict(self):
        return {
            'id': self.id,
            'owner': self.owner,
            'title': self.title,
            'description': self.description,
            'status': self.status,
        }
