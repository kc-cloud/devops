from flask import Flask, jsonify, flash, request
import pymysql
from flaskext.mysql import MySQL
import os
import hashlib

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ['db_username']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['db_password']
app.config['MYSQL_DATABASE_DB'] = os.environ['db_name']
app.config['MYSQL_DATABASE_HOST'] = os.environ['db_host']
mysql.init_app(app)

@app.route('/')
def index():
	return "Flask Tutorial"

@app.route('/users/add', methods=['POST'])
def add_user():
	conn = None
	response_payload = jsonify('No data found')
	try:
		request_payload = request.json
		user_name = request_payload['name']
		user_email = request_payload['email']
		user_password = request_payload['password']
		if user_name and user_email and user_password and request.method == 'POST':
			hashed_pwd = hashlib.md5(user_password.encode()).hexdigest()
			sql = "INSERT INTO users(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (user_name, user_email, hashed_pwd,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			response_payload = jsonify('User added successfully!')
			response_payload.status_code = 200
		else:
			response_payload = not_found()
	except Exception as e:
		response_payload = jsonify(e)
	finally:
		if conn:
			conn.close()
	return response_payload
		
@app.route('/users')
def users():
	conn = None
	response_payload = jsonify('No data found')
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users")
		rows = cursor.fetchall()
		if rows and len(rows) > 0:
			response_payload = jsonify(rows)
		response_payload.status_code = 200
	except Exception as e:
		response_payload = jsonify(e)
	finally:
		if conn:
			conn.close()
	return response_payload
		
@app.route('/users/<id>')
def user(id):
	conn = None
	response_payload = jsonify('No data found')
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row and len(row) > 0:
			response_payload = jsonify(row)
		response_payload.status_code = 200
	except Exception as e:
		response_payload = jsonify(e)
	finally:
		if conn:
			conn.close()
	return response_payload

@app.route('/users/update', methods=['POST'])
def update_user():
	conn = None
	response_payload = jsonify('No record updated')
	try:
		request_payload = request.json
		user_id = request_payload['id']
		user_name = request_payload['name']
		user_email = request_payload['email']
		user_password = request_payload['password']		
		if user_name and user_email and user_password and user_id and request.method == 'POST':
			hashed_pwd = hashlib.md5(user_password.encode()).hexdigest()
			sql = "UPDATE users SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (user_name, user_email, hashed_pwd, user_id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			response_payload = jsonify('User updated successfully!')
			response_payload.status_code = 200
		else:
			response_payload = not_found()
	except Exception as e:
		response_payload = jsonify(e)
	finally:
		if conn:
			conn.close()
	return response_payload
		
@app.route('/users/delete/<id>')
def delete_user(id):
	conn = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM users WHERE user_id=%s", (id,))
		conn.commit()
		response_payload = jsonify('User deleted successfully!')
		response_payload.status_code = 200
	except Exception as e:
		response_payload = jsonify(e)
	finally:
		if conn:
			conn.close()
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
