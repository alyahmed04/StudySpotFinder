from Models.User import User
from Models.Spot import Spot
from Models.Review import Review
from Database_Operations.UserDB import UserDB
from Database_Operations.SpotDB import SpotDB
from Database_Operations.ReviewDB import ReviewDB
import unittest
import mysql.connector

#learned about unit test order from 
#https://stackoverflow.com/questions/4095319/unittest-tests-order
unittest.TestLoader.sortTestMethodsUsing = None

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'studyspot',
  'raise_on_warnings': True
}

#Learned how to unit test SQL commands from this source:
#https://www.freecodecamp.org/news/testing-and-debugging-sql-queries-with-python/

#learned about unit test order from 
#https://stackoverflow.com/questions/4095319/unittest-tests-order

#SQL commands learned from under various pages
#https://www.w3schools.com/python/python_mysql_where.asp

class test_SQL_commands(unittest.TestCase):        

    def test_01_create_studyspot(self):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        # Create a study spot
        print("1. Creating a study spot")
        SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")

        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Newman Library'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        expected = (1, "Newman Library", "560 Drillfield Dr, Blacksburg, VA")
        self.assertEqual(result[1], expected[1])
        self.assertEqual(result[2], expected[2])

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM study_spots WHERE spotName = 'Newman Library'")

        db.commit()
        cursor.close()
        db.close()

    def test_02_create_user(self):
        # Create a user
        print("2. Creating a user")
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        UserDB.create_user(
            username="testuser5",
            email="test5@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
        )

        cursor.execute("SELECT * FROM users WHERE username = 'testuser5'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        print(result)
        expected = (1, "testuser5", "test5@vt.edu", "testPassword", None, 0)
        self.assertEqual(result[1], expected[1])
        self.assertEqual(result[2], expected[2])
        self.assertEqual(result[3], expected[3])
        self.assertEqual(result[4], expected[4])
        self.assertEqual(result[5], expected[5])

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM users WHERE username = 'testuser5'")

        db.commit()

        cursor.close()
        db.close()

    def test_03_create_review(self):
        print("3. Creating a review")

        UserDB.create_user(
            username="testuser2",
            email="test2@vt.edu",
            password="testPassword",
            favoriteStudySpot=None, 
            kudos=0
        )

        SpotDB.create_spot("New", "580 Drillfield Dr, Blacksburg, VA")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = 'testuser2'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        userRes = cursor.fetchone()

        user = User(userID=userRes[0],username="testuser2",email="test2@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0)

        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'new'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        spotRes = cursor.fetchone()

        spot = Spot(spotID=spotRes[0],spotName="New",location="580 Drillfield Dr, Blacksburg, VA")

        cursor.close()
        db.close()

        ReviewDB.create_review(starRating = 4, noiseLevel = 7, content = "Test content", crowdedness = 7, user = user, spot = spot)

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM spot_reviews;")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        expected = (1, spot.spotID, user.userID, 7, 7, 4, "Test content")
        self.assertEqual(result[1], expected[1])
        self.assertEqual(result[2], expected[2])
        self.assertEqual(result[3], expected[3])
        self.assertEqual(result[4], expected[4])
        self.assertEqual(result[5], expected[5])
        self.assertEqual(result[6], expected[6])
  
        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM users WHERE username = 'testuser2'")
        cursor.execute("DELETE FROM study_spots WHERE spotName = 'New'")

        db.commit()

        cursor.close()
        db.close()

    def test_04_edit_spot_name(self):

        # Edit the name of a study spot

        print("4. Editing a spot's name")

        SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Newman Library'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        spotRes = cursor.fetchone()
    
        spot = Spot(spotID=spotRes[0],spotName="Newman Library",location="560 Drillfield Dr, Blacksburg, VA")

        cursor.close()
        db.close()
        SpotDB.edit_spot_name(spot, "Newman")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        #learned from:
        #https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
        value = tuple([spotRes[0],])

        cursor.execute("SELECT * FROM study_spots WHERE spotID = %s", value)

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        expected = (spotRes[0], "Newman", "560 Drillfield Dr, Blacksburg, VA")
        self.assertEqual(result, expected)

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM study_spots WHERE spotID = %s", value)

        db.commit()

        cursor.close()
        db.close()

    def test_05_edit_spot_location(self):

        # Edit the name of a study spot
       
        print("4. Editing a spot's name")

        SpotDB.create_spot("man", "560 Drillfield Dr, Blacksburg, VA")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'man'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        spotRes = cursor.fetchone()

        spot = Spot(spotID=spotRes[0],spotName="man",location="560 Drillfield Dr, Blacksburg, VA")

        cursor.close()
        db.close()
        SpotDB.edit_spot_location(spot, "570 Drillfield Dr, Blacksburg, VA")
        
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'man'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        expected = (spotRes[0], "man", "570 Drillfield Dr, Blacksburg, VA")
        self.assertEqual(result, expected)

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM study_spots WHERE spotName = 'man'")
        
        db.commit()

        cursor.close()
        db.close()
        

if __name__ == "__main__":
    unittest.main()