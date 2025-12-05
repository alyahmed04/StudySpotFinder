import mysql.connector
from mysql.connector import pooling

#Learned from the following sources about sql and mysqlconnector
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
#https://www.w3schools.com/python/python_mysql_update.asp
#https://www.red-gate.com/simple-talk/databases/mysql/modifying-mysql-data-from-within-python/

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'studyspot',
  'raise_on_warnings': True
}

# Creates a connection pool, pool_size of 5 is more than sufficient for testing
connection_pool = pooling.MySQLConnectionPool(
    pool_name = "studyspot_pool",
    pool_size = 5,
    **config
)

def execute_DBOperation(command, value):
        conn = connection_pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(command, value)
        conn.commit()
        cursor.close()
        conn.close()