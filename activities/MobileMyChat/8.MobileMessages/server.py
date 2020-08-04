import time
from flask import Flask, request, render_template, redirect
import json
from Extras import database, encoder, cruds

app = Flask(__name__)
app.secret_key = "You Will Never Guess"


# Before all, set messages and users
@app.before_first_request
def setall():
    database.setmessages()
    database.setusers()
    return


# For web app
@app.route('/')
def login():
    return render_template('Login.html')


# To show any html file (specially crud_messages.html)
@app.route('/static/<content>')
def display_template(content):
    return render_template(content)


# For web and mobile app
# ---------------------------------------- Login validator --------------------------------------------
@app.route('/dologin', methods=['POST', 'GET'])
def dologin():
    if request.method == 'POST':
        database.setusers()
        user = request.form['user']
        passw = request.form['pass']

        # From android
        if request.headers.get("User-Agent") == "android":
            if user in database.cacheusers and passw == database.cacheusers[user][0]:
                return 'good'
            else:
                return 'bad'

        # From not android
        else:
            if user in database.cacheusers and passw == database.cacheusers[user][0]:
                database.cacheusers = {}
                return render_template('Chat.html')
            else:
                time.sleep(1)  # Just to show js animation
                return redirect("/")  # Return to Login.html


# ---------------------------------------- CRUD Messages --------------------------------------------
# Get all messages
@app.route('/messages', methods=['GET'])
def crudmessages_get():
    return cruds.get_messages()


# Add new message
@app.route('/messages', methods=['POST'])
def crudmessages_post():
    return cruds.create_message()


# Delete message by id
@app.route('/messages', methods=['DELETE'])
def crudmessages_delete():
    return cruds.remove_message()


# Update message by id
@app.route('/messages', methods=['PUT'])
def crudmessages_put():
    return cruds.update_message()


# Get message by id (not needed by crud_messages)
@app.route('/messages/<id>', methods=['GET'])
def get_message(id):
    messagey = database.session.query(database.Message).filter(database.Message.id == id)
    for m in messagey:
        js = json.dumps(m, cls=encoder.AlchemyEncoder)
        return Response(js, status=200, mimetype='application/json')

    etc = {"status": 404, "message": "Not Found"}
    return Response(etc, status=404, mimetype='application/json')


# ---------------------------------------- CRUD Users --------------------------------------------

# Get all users
@app.route('/users', methods=['GET'])
def crudusers_get():
    database.setusers()
    return cruds.get_users()


# Add new message
@app.route('/users', methods=['POST'])
def crudusers_post():
    return cruds.create_user()


# Delete message by id
@app.route('/users', methods=['DELETE'])
def crudusers_delete():
    return cruds.remove_user()


# Update message by id
@app.route('/users', methods=['PUT'])
def crudusers_put():
    return cruds.update_user()


# Get message by id (not needed by crud_messages)
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    usery = database.session.query(database.User).filter(database.User.id == id)
    for u in usery:
        js = json.dumps(u, cls=encoder.AlchemyEncoder)
        return Response(js, status=200, mimetype='application/json')

    etc = {"status": 404, "message": "Not Found"}
    return Response(etc, status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run()
