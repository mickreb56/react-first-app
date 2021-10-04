from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123',
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222',
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999',
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users

   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd["id"] = str(uuid.uuid1())
      users['users_list'].append(userToAdd)
      resp = jsonify(data = userToAdd,sucess=True)
      resp.status_code=201
      return resp

   elif request.method == 'DELETE':
      userToRemove = request.get_json()
      users['users_list'].remove(userToRemove)
      rest = jsonify(success=True)
      return rest

@app.route('/users/<id>', methods=['GET','DELETE'])
def get_user(id):

   if request.method == "GET":
      if id :
         for user in users['users_list']:
            if user['id'] == id:
               return user
         return ({})
      return users
   elif request.method == "DELETE":
      print("trying to delete user: " + id)
      for user in users['users_list']:
         if user["id"] == id:
            users['users_list'].remove(user)
            resp = jsonify(data=users, success=True)
            resp.status_code = 204
            return resp
      resp = jsonify(data=users, success=False)
      resp.status_code = 404
      return resp
   return users

@app.route('/users/<id>/<name>')
def get_alluser(name, id):
    subdict = {'users_list' : []}
    if id :
        for user in users['users_list']:
            if user['name'] == name and user['id'] == id:
                subdict['users_list'].append(user)
        if subdict:
            return subdict
    return ({})








