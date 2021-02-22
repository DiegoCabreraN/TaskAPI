from flask import jsonify
from app import db
from tasks.models import Task


def getTask(id):
    query = db.session.query(Task)
    query = query.filter(Task.id == id)
    retrievedTask = query.first()
    return retrievedTask.as_dict()


def deleteTask(id):
    query = db.session.query(Task)
    query = query.filter(Task.id == id)
    retrievedTask = query.first()
    db.session.delete(retrievedTask)
    db.session.commit()
    return {'Deleted Task': retrievedTask.as_dict()}


def getTasks(user_id):
    query = db.session.query(Task)
    query = query.filter(getattr(Task, "owner") == user_id)
    rows = query.all()
    tasks = [row.as_dict() for row in rows]

    return tasks


def createTask(taskData):
    try:
        task = Task(
            owner=taskData['user_id'],
            title=taskData['title'],
            description=taskData['description'],
            status=False
        )
        db.session.add(task)
        db.session.commit()
        return 'Task Created Successfully', 200
    except Exception:
        return 'Error while creating the task', 500


def updateTask(id, taskDictionary):
    try:
        task = Task.query.filter_by(id=id)
        task.update(dict(
            owner=taskDictionary['user_id'],
            title=taskDictionary['title'],
            description=taskDictionary['description'],
            status=taskDictionary['status'],
        ))
        db.session.commit()
        return 'Task Updated Successfuly', 200
    except Exception:
        return 'Error while updating the task', 500

