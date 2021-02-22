from app import db
from auth.models import User


def createUser(username, email, password):
    try:
        #Check username and email
        nameOnDatabase = User.query.filter_by(username=username).first()
        mailOnDatabase = User.query.filter_by(email=email).first()
        if nameOnDatabase:
            return 'Username is already taken', 500
        if mailOnDatabase:
            return 'Mail is already taken', 500
        #Add user
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'User created', 200
    except Exception:
        return 'Error on server', 500


def loginUser(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return { "id": user.id}, 200
    return 'Wrong Username or Password', 500