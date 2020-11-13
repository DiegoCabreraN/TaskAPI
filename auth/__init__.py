from app import db
from auth.models import User


def createUser(username, email, password):
    try:
        nameOnDatabase = User.query.filter_by(username=username).first()
        mailOnDatabase = User.query.filter_by(email=email).first()
        print(nameOnDatabase)

        if nameOnDatabase:
            return 'Username is already taken', 500
        if mailOnDatabase:
            return 'Mail is already taken', 500

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'User created', 200
    except Exception:
        return 'Error on server', 500


def searchUser(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            return 'Authorized Login', 200
        else:
            return 'Wrong Password', 500
    else:
        return 'Wrong Username', 500


def userExists(username):
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            return True
    return False
