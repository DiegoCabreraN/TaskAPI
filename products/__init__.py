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
            image=productData['image'],
            score=0,
            reviews=0
        )
        db.session.add(product)
        db.session.commit()
        return 'Product Created Successfuly', 200
    except Exception:
        return 'Error while creating the product', 500


def updateProduct(id, productDictionary):
    try:
        product = Product.query.filter_by(id=id)
        product.update(dict(
            name=productDictionary['name'],
            style=productDictionary['style'],
            color=productDictionary['color'],
            gender=productDictionary['gender'],
            price=productDictionary['price'],
            description=productDictionary['description'],
            image=productDictionary['image'],
        ))
        db.session.commit()
        return 'Product Updated Successfuly', 200
    except Exception:
        return 'Error while updating the product', 500


def setScore(id, scoreToAdd):
    # try:
    product = Product.query.filter_by(id=id)
    productDictionary = product.first().as_dict()
    totalScore = productDictionary['reviews'] * productDictionary['score']
    productDictionary['reviews'] += 1

    newScore = totalScore + int(scoreToAdd)
    productDictionary['score'] = newScore/productDictionary['reviews']
    
    product.update(dict(
            score=productDictionary['score'],
            reviews=productDictionary['reviews'],
        ))

    db.session.commit()
    return 'Score Updated Successfuly', 200
    # except Exception:
    #     return 'Error while updating the score', 500
