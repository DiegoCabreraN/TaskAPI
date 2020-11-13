from app import db
from checkout.models import Checkout


def createOrder(orderData):
    try:
        order = Checkout(
            username=orderData['username'],
            address=orderData['address'],
            country=orderData['country'],
            lastNums=orderData['lastNums'],
            total=orderData['total'],
            itemList=orderData['itemList'],
        )
        db.session.add(order)
        db.session.commit()
        return 'Order Created Successfuly', 200
    except Exception:
        return 'Error while creating the order', 500


def getOrders(username):
    query = db.session.query(Checkout)
    query = query.filter(Checkout.username == username).all()
    return query
