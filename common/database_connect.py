import pymysql.cursors


## This script contains all functions for accessing a mySQL database:
## 1. Select Statements
## 2. Insert Statements

class MySQLConn:
	def __init__(self,host,port,user,pw,schema):
		self.host=host
		self.port=int(port)
		self.user=user
		self.pw=pw
		self.db=schema

	def SelectQuery(self,query):
		connection= pymysql.connect(host=self.host,
									port=self.port,
		                             user=self.user,
		                             password=self.pw,
		                             db=self.db,
		                             use_unicode=True,
		                             charset='utf8',
		                             cursorclass=pymysql.cursors.DictCursor)
		results=''
		try:
			with connection.cursor() as cursor:
				num_of_rows=cursor.execute(query)
				results=cursor.fetchall()
		finally:
				connection.close()
		return results


	def InsertQuery(self,query):
		connection= pymysql.connect(host=self.host,
									port=self.port,
		                            user=self.user,
		                            password=self.pw,
		                            db=self.db,
		                            use_unicode=True,
		                            charset='utf8',
		                            cursorclass=pymysql.cursors.DictCursor)
		result=''
		try:
			with connection.cursor() as cursor1:
				cursor1.execute('SET NAMES utf8;')
				cursor1.execute('SET CHARACTER SET utf8;')
				cursor1.execute('SET character_set_connection=utf8;')				
				if(len(query) > 1):
					cursor1.execute(query)
					connection.commit()
					result=1
				else:
					result=0
		finally:
			connection.close()
		return result