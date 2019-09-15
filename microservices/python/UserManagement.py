from flask import Flask, jsonify, flash, request
import pymysql
from flaskext.mysql import MySQL
import os
import hashlib

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
# os.environ['db_username']= 'root'
# os.environ['db_password'] = 'welcome1'
# os.environ['db_name'] = 'DEVOPS_USERS'
# os.environ['db_host'] = 'devops-mysql'

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
			return response_payload
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users")
		rows = cursor.fetchall()
		response_payload = jsonify(rows)
		response_payload.status_code = 200
		return response_payload
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		
@app.route('/users/<id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users WHERE user_id=%s", id)
		row = cursor.fetchone()
		response_payload = jsonify(row)
		response_payload.status_code = 200
		return response_payload
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/users/update', methods=['POST'])
def update_user():
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
			return response_payload
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/users/delete/<id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM users WHERE user_id=%s", (id,))
		print ('deleted')
		conn.commit()
		print ('committed')
		response_payload = jsonify('User deleted successfully!')
		response_payload.status_code = 200
		return response_payload
	except Exception as e:
		print(e)
	finally:
		if conn:
			conn.close()
		
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
    app.run()
