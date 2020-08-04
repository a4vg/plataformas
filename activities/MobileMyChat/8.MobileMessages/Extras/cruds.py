import json
import database
import encoder
from flask import request

#-----------------------------  CRUD MESSAGES -----------------------------------------------------


def get_messages():
    response = []
    for m in database.session.query(database.Message):
        response.append(m)
    return json.dumps(response, cls=encoder.AlchemyEncoder)


def create_message():
    c = request.get_json(silent=True)
    newmessage = json.loads(request.form["values"])
    if newmessage["id"] not in database.cachemessages:
        message = database.Message(id=newmessage['id'], sendby=newmessage['sendby'],
                                   receiveby=newmessage['receiveby'], message=newmessage['message'])
        database.session.add(message)
        database.session.commit()

        for i in newmessage:
            database.cachemessages[newmessage["id"]] = [newmessage['sendby'],
                                                        newmessage['receiveby'], newmessage['message']]

        return 'Message created'
    return "The id is already in use"


def remove_message():
    id = request.form["key"]
    message = database.session.query(database.Message).filter(database.Message.id == id)
    print("----BEFORE-----------------------", database.cachemessages)
    database.cachemessages.pop(int(id), None)
    print("------AFTER---------------------", database.cachemessages)
    for m in message:
        database.session.delete(m)
    database.session.commit()
    return "DELETED"

    etc = {"status": 404, "message": "Not Found"}
    return Response(etc, status=404, mimetype='application/json')


def update_message():
    id = request.form["key"]
    message = database.session.query(database.Message).filter(database.Message.id == id).first()

    if message == None:
        etc = {"status": 404, "message": "Not Found"}
        return Response(etc, status=404, mimetype='application/json')

    update = json.loads(request.form['values'])

    for key in update.keys():
        setattr(message, key, update[key])
        #message.key = update[key]

    return "MESSAGE UPDATED"


#-----------------------------  CRUD USERS -----------------------------------------------------


def get_users():
    response = []
    for u in database.session.query(database.User):
        response.append(u)

    print("Esta es el response: ", response)
    return json.dumps(response, cls=encoder.AlchemyEncoder)


def create_user():
    c = request.get_json(silent=True)
    newuser = json.loads(request.form["values"])
    if newuser["id"] not in database.cacheusers:
        user = database.User(id=newuser['id'], username=newuser['username'],
                             password=newuser['password'], fullname=newuser['fullname'])
        database.session.add(user)
        database.session.commit()

        for i in newuser:
            database.cachemessages[newuser["id"]] = [newuser['username'],
                                                     newuser['password'], newuser['fullname']]

        return 'User created'
    return "The id is already in use"


def remove_user():
    id = request.form["key"]
    user = database.session.query(database.User).filter(database.User.id == id)
    print("----BEFORE-----------------------", database.cacheusers)
    database.cacheusers.pop(int(id), None)
    print("------AFTER---------------------", database.cacheusers)
    for u in user:
        database.session.delete(u)
    database.session.commit()
    return "DELETED"

    etc = {"status": 404, "message": "Not Found"}
    return Response(etc, status=404, mimetype='application/json')


def update_user():
    id = request.form["key"]
    user = database.session.query(database.User).filter(database.User.id == id).first()

    if user == None:
        etc = {"status": 404, "message": "Not Found"}
        return Response(etc, status=404, mimetype='application/json')

    update = json.loads(request.form['values'])

    for key in update.keys():
        setattr(user, key, update[key])
        #user.key = update[key]

    return "USER UPDATED"
