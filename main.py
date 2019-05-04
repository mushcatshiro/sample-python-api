import pymysql
import datetime
import json
import falcon
import information


conn = pymysql.connect(host=information.host, database=information.database, user=information.user, password=information.password)
conn_cursor = conn.cursor()
# conn_cursor.execute("""CREATE TABLE customers (customer_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
# 											  customer_name VARCHAR(50),
# 											  customer_dob DATE,
# 											  customer_update_at DATETIME)
# 	""")


class create_customers:
	def on_get(self, req, resp):
		data = json.loads(req.stream.read())
		# print(data['customer_name'], data['customer_dob'])
		# change json to python dict
		insert_tuple = (data['customer_name'], data['customer_dob'])
		try:
			with conn:
				conn_cursor.execute("INSERT INTO customers (customer_id, customer_name, customer_dob, customer_update_at) VALUES (NULL, %s, %s, now())",insert_tuple)
				info ={}
				info['message'] = 'added'
				resp.body = json.dumps(info)
		except:
			info ={}
			info['message'] = 'error'
			resp.body = json.dumps(info)

class read_customers:
	def on_get(self, req, resp):
		data = json.loads(req.stream.read())
		insert_tuple = (data['customer_name'])
		# if insert_tuple == 'all':
		# 	conn_cursor.execute("SELECT * FROM customers")
		# 	result = conn_cursor.fetchall()
		# 	info = {}
		# 	n = 0
		# 	for row in result:
		# 		print(row)
		# 		info['query'] = row[n]
		# 		n+=1
		# 	print(info)
		# else:
		with conn:
			try:
				conn_cursor.execute("SELECT * FROM customers WHERE customer_name = %s", insert_tuple)
				result = conn_cursor.fetchall()
				# print(result)
				info = {}
				info["ID"] = result[0][0]
				info["Name"] = result[0][1]
				info["DOB"] = str(result[0][2])
				info["Last_Update"] = str(result[0][3])
				resp.body = json.dumps(info)
			except:
				info = {}
				info["message"] = 'error'
				resp.body = json.dumps(info)

class delete_customers:
	def on_get(self, req, resp):
		data = json.loads(req.stream.read())
		insert_tuple = (data['customer_name'])
		with conn:
			try:
				conn_cursor.execute("DELETE FROM customers WHERE customer_name = %s", (insert_tuple,))
				info = {}
				info["message"] = 'updated'
				# suppossely to be only deleting exist entries and print delete success
				resp.body = json.dumps(info)
			except:
				pass
				# conn_cursor.execute("SELECT * FROM customers")
				# result = conn_cursor.fetchall()
				# print(result)
			# except:
			# 	conn_cursor.execute("SELECT * FROM customers")
			# 	result = conn_cursor.fetchall()
			# 	print(result)
			# 	info = {}
			# 	info["message"] = 'no such entry'
			# 	resp.body = json.dumps(info)

class update_customers:
	def on_get(self, req, resp):
		data = json.loads(req.stream.read())
		dob = (data['customer_dob'])
		name = (data['customer_name'])
		idno = (data['customer_id'])
		with conn:
			try:
				conn_cursor.execute("UPDATE customers SET customer_dob = %s WHERE customer_name = %s AND customer_id = %s", (dob, name, idno))
				info = {}
				info["message"] = 'updated'
				# supposely to only update exist entries
				resp.body = json.dumps(info)
			except:
				pass
				# conn_cursor.execute("SELECT * FROM customers")
				# result = conn_cursor.fetchall()
				# print(result)
			# except:
			# 	conn_cursor.execute("SELECT * FROM customers")
			# 	result = conn_cursor.fetchall()
			# 	print(result)
			# 	info = {}
			# 	info["message"] = 'no update'
			# 	resp.body = json.dumps(info)

api = falcon.API()
api.add_route('/create', create_customers())
api.add_route('/read', read_customers())
api.add_route('/delete', delete_customers())
api.add_route('/update', update_customers())