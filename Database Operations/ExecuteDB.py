import mysql.connector

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