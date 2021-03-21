import json
from flask import request, jsonify, Response
from flask_cors import cross_origin
from app.config import app, db

from auth import (
    createUser,
    loginUser,
)

from tasks import (
    getTasks,
    createTask,
    getTask,
    deleteTask,
    updateTask,
)


@app.route('/signup', methods=['POST'])
def signUp():
    response = createUser(
        request.json['username'],
        request.json['email'],
        request.json['password'],
    )
    return response

@app.route('/login', methods=['POST'])
def login():
    response =  loginUser(
        request.json['username'],
        request.json['password']
    )
    return response

@app.route('/tasks', methods=['GET', 'POST'])
@cross_origin()
def tasks():
    if request.method == 'GET':
        user_id = request.args.get('user_id', type=int)
        tasks = getTasks(user_id)
        return Response(json.dumps(tasks), mimetype='application/json')
    else:
        response = createTask(request.json)
        return response


@app.route('/tasks/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def task(id):
    actualTask = getTask(id)
    if request.method == 'GET':
            user_id = request.args.get('user_id', type=int)
            if actualTask['owner'] == user_id:
                return Response(json.dumps(actualTask), mimetype='application/json'), 200
            else:
                return "Oops!, something went wrong", 404
                
    elif actualTask['owner'] == request.json['user_id']:
        elif request.method == 'PUT':
            taskDictionary = {
                'id': request.json.get('id', actualTask['id']),
                'title': request.json.get('title', actualTask['title']),
                'description': request.json.get('description', actualTask['description']),
                'status': request.json.get('status', actualTask['status']),
            }
            response = updateTask(id, taskDictionary)
            return response
        else:
            deletedTask = deleteTask(id)
            return Response(json.dumps(deletedTask), mimetype='application/json'), 200
    else:
        return "Oops!, something went wrong", 404

db.create_all()
