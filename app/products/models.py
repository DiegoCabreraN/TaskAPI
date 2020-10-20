from app import db

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  style = db.Column(db.String(30), nullable=False)
  color = db.Column(db.String(30), nullable=False)
  gender = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(250), nullable=False)

  def __repr__(self):
    return '<Product {}>'.format(self.name)

  def as_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'style': self.style,
      'color': self.color,
      'gender': self.gender,
      'price': self.price,
      'description': self.description
    }