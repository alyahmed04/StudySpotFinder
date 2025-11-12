import mysql.connector
from Models.Spot import Spot

config = {
  'user': 'placeholder',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'studyspot',
  'raise_on_warnings': True
}

db = mysql.connector.connect(**config)

# create_review = ("INSERT INTO review "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")

# edit_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")

class SpotDB:

    def create_spot(spot: Spot):
       
        print("hello")
        #ccreate
        

    def edit_spot_location(spot: Spot):

        print("hello")
        #sometjhng 


    def delete_spot(spot: Spot):
        print("hello")
        print("hello")
        #sometjhng

db.close()