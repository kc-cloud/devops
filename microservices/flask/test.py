from flask import Flask, jsonify, flash, request
import os

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return "Flask Tutorial"

@app.route('/users/add', methods=['POST'])
def add_user():
    request_payload = request.json
    user_name = request_payload['name']
    user_email = request_payload['email']
    user_address = request_payload['address']
    user_city = request_payload['city']
    user_state = request_payload['state']
    if user_name and user_email and user_address and user_city and user_state and request.method == 'POST':
        users[user_name]= {'name': user_name,'email': user_email, 'address': user_address, 'city': user_city, 'state': user_state}
        response_payload = jsonify('User added successfully!')
        response_payload.status_code = 200
        return response_payload
    else:
        message = {'message': 'No user records Found'}
        response_payload = jsonify(message)
        response_payload.status_code = 200
        return response_payload
        
@app.route('/users')
def list_users():
    if users:
        print (users)
        response_payload = jsonify(users)
    else:
        message = {'message': 'No user records Found'}
        response_payload = jsonify(message)
    response_payload.status_code = 200
    return response_payload

@app.route('/users/<name>')
def user(name):
    row = users[name]
    response_payload = jsonify(row)
    response_payload.status_code = 200
    return response_payload

@app.route('/users/update', methods=['POST'])
def update_user():
    request_payload = request.json

    if 'email' in request_payload:
        users[request_payload['name']]['email'] = request_payload['email'] 
    if 'address' in request_payload:
        users[request_payload['name']]['address'] = request_payload['address'] 
    if 'city' in request_payload:
        users[request_payload['name']]['city'] = request_payload['city']
    if 'state' in request_payload:
        users[request_payload['name']]['state'] = request_payload['state']
    response_payload = jsonify('User updated successfully!')
    response_payload.status_code = 200
    return response_payload

@app.route('/users/delete/<name>')
def delete_user(name):
    del users[name]
    response_payload = jsonify({'message': 'User deleted successfully!'})
    response_payload.status_code = 200
    return response_payload
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response_payload = jsonify(message)
    response_payload.status_code = 404

    return response_payload
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
