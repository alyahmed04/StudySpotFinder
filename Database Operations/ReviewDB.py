import mysql.connector
from Models.Review import Review

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

class UserDB:

    def create_review(review: Review):
       
        print("hello")
        #ccreate
        

    def edit_post_rating(review: Review):

        print("hello")
        #sometjhng 



    def edit_post_content(review: Review):

        print("hello")
        #sometjhng 


    def delete_review(review: Review):
        print("hello")
        print("hello")
        #sometjhng

db.close()