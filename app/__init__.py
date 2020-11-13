import json
from flask import request, jsonify, Response
from app.config import app, db
from auth import createUser, searchUser, userExists
from products import getProducts, createProduct, getProduct, deleteProduct
from checkout import getOrders, createOrder


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
                .replace('(', '')\
                .replace(')', '')\
                .split(',')
        products = getProducts(params)
        return Response(json.dumps(products), mimetype='application/json')
    else:
        productData = {
            'name': request.args['name'],
            'style': request.args['style'],
            'color': request.args['color'],
            'gender': request.args['gender'],
            'price': request.args['price'],
            'description': request.args['description'],
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


@app.route('/checkouts', methods=['GET', 'POST'])
def checkouts():
    if request.method == 'GET':
        username = request.args.get('username', None)
        if userExists(username):
            raw_orders = getOrders(username)
            orders = []
            for order in raw_orders:
                data = order.as_dict()
                data['itemList'] = json.loads(data['itemList'])
                orders.append(data)
            res_type = 'application/json'
            response = Response(json.dumps(orders), mimetype=res_type)
            return response, 200
        else:
            return 'Username not found', 404
    else:
        orderData = {
            'username': request.args['username'],
            'address': request.args['address'],
            'country': request.args['country'],
            'lastNums': request.args['lastNums'],
            'total': request.args['total'],
            'itemList': request.data,
        }
        
        return createOrder(orderData)


db.create_all()
