import json
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SERVER_NAME'] = "localhost:8000"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sunshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print('LISTENING ON PORT 8000')

from app.auth import createUser, searchUser

@app.route('/signup', methods=['POST'])
def signUp():
  return createUser(
    request.args['username'],
    request.args['email'],
    request.args['password']
  )

@app.route('/login', methods=['POST'])
def login():
  return searchUser(
    request.args['username'],
    request.args['password']
  )

from app.products import getProducts, createProduct, getProduct, deleteProduct

@app.route('/products', methods=['GET', 'POST'])
def products():
  if request.method == 'GET':
    params = {
      'gender': request.args.get('gender', 0),
      'color': request.args.get('color', None),
      'style': request.args.get('style', None),
      'price': request.args.get('priceRange', None)
    }
    if params['price']:
      params['price'] = params['price']\
        .replace('(','')\
        .replace(')','')\
        .split(',')
    products = getProducts(params)
    return Response(json.dumps(products), mimetype='application/json')
  else:
    productData = {
      'name' : request.args['name'],
      'style' : request.args['style'],
      'color' : request.args['color'],
      'gender' : request.args['gender'],
      'price' : request.args['price'],
      'description' : request.args['description'],
    }
    return createProduct(productData)

@app.route('/products/<int:id>', methods=['GET', 'DELETE'])
def product(id):
  if request.method == 'GET':
    product = getProduct(id)
    return Response(json.dumps(product), mimetype='application/json'), 200
  else:
    product = deleteProduct(id)
    return Response(json.dumps(product), mimetype='application/json'), 200

db.create_all()