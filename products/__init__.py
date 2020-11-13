from flask import jsonify
from app import db
from products.models import Product


def getProduct(id):
    query = db.session.query(Product)
    query = query.filter(Product.id == id)
    retrievedProduct = query.first()
    return retrievedProduct.as_dict()


def deleteProduct(id):
    query = db.session.query(Product)
    query = query.filter(Product.id == id)
    retrievedProduct = query.first()
    db.session.delete(retrievedProduct)
    return {'Deleted Object': retrievedProduct.as_dict()}


def getProducts(params):
    query = db.session.query(Product)
    for k, v in params.items():
        if k != 'price' and v:
            query = query.filter(getattr(Product, k) == v)
        elif v:
            query = query.filter(getattr(Product, k) >= v[0])\
                .filter(getattr(Product, k) <= v[1])
    rows = query.all()

    products = [row.as_dict() for row in rows]

    return products


def createProduct(productData):
    try:
        product = Product(
            name=productData['name'],
            style=productData['style'],
            color=productData['color'],
            gender=productData['gender'],
            price=productData['price'],
            description=productData['description'],
        )
        db.session.add(product)
        db.session.commit()
        return 'Product Created Successfuly', 200
    except Exception:
        return 'Error while creating the product', 500
