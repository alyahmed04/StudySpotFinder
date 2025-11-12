import mysql.connector
from Models.User import User

config = {
  'user': 'placeholder',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'studyspot',
  'raise_on_warnings': True
}


class UserDB:

    def create_user(user: User):
        db = mysql.connector.connect(**config)
        print("hello")
        #ccreate
        db.close()

    def compare_user_creditentials(user: User):
        db = mysql.connector.connect(**config)
        print("hello")
        print("hello")
        #sometjhng 
        db.close()

    def edit_username(user: User):
        db = mysql.connector.connect(**config)
        print("hello")
        #sometjhng 
        db.close()


    def edit_favorite_study_spot(user: User):
        db = mysql.connector.connect(**config)
        print("hello")
        #sometjhng 
        db.close()

    def delete_user(user: User):
        db = mysql.connector.connect(**config)
        print("hello")
        print("hello")
        #sometjhng
        db.close()