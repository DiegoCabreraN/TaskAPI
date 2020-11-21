from app import db
from auth.models import User


def createUser(username, email, password):
    try:
        nameOnDatabase = User.query.filter_by(username=username).first()
        mailOnDatabase = User.query.filter_by(email=email).first()
        if nameOnDatabase:
            return 'Username is already taken', 500
        if mailOnDatabase:
            return 'Mail is already taken', 500

        user = User(role=0, username=username, email=email, password=password)
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


def createSuperUser(username, email, password):
    try:
        nameOnDatabase = User.query.filter_by(username=username).first()
        mailOnDatabase = User.query.filter_by(email=email).first()
        if nameOnDatabase:
            return 'Username is already taken', 500
        if mailOnDatabase:
            return 'Mail is already taken', 500

        user = User(role=1, username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Super User created', 200
    except Exception:
        return 'Error on server', 500


def userIsSuperUser(username):
    if username:
        user = User.query.filter_by(username=username).first()
        if user and user.role == 1:
            return 'Is Super User!', 200
    return 'Is Not Super User', 400
