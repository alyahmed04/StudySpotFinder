import mysql.connector

#Learned from the following sources about sql and mysqlconnector
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
#https://www.w3schools.com/python/python_mysql_update.asp
#https://www.red-gate.com/simple-talk/databases/mysql/modifying-mysql-data-from-within-python/

config = {
  'user': 'placeholder',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'studyspot',
  'raise_on_warnings': True
}


def execute_DBOperation(command, value):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute(command, value)
        db.commit()
        cursor.close()
        db.close()