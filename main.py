from Models.User import User
from Models.Spot import Spot
from Models.Review import Review
from Database_Operations.UserDB import UserDB
from Database_Operations.SpotDB import SpotDB
from Database_Operations.ReviewDB import ReviewDB
import unittest
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'studyspot',
  'raise_on_warnings': True
}

#Learned how to unit test SQL commands from this source:
#https://www.freecodecamp.org/news/testing-and-debugging-sql-queries-with-python/

class test_SQL_commands(unittest.TestCase):
    def test_create_studyspot(self):
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        # Create a study spot
        print("1. Creating a study spot")
        SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")
        cursor.execute("SELECT * FROM study_spots;")
        result = cursor.fetchall()
        expected = [(1, "Newman Library", "560 Drillfield Dr, Blacksburg, VA")]
        self.assertEqual(result, expected)
       
        cursor.close()
        db.close()
        
    def test_create_user(self):
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

        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()
        expected = [(1, "testuser5", "test5@vt.edu", "testPassword", None, 0)]
        self.assertEqual(result, expected)

       
        cursor.close()
        db.close()

    def test_create_review(self):
        print("3. Creating a review")
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        user = User()
        user.userID = 1
        user.username = "testuser5"
        user.email = "test5@vt.edu"
        user.password = "testPassword"
        user.favoriteStudySpot = None
        user.kudos = 0

        spot = Spot()
        spot.spotID = 1
        spot.spotName = "Newman Library"
        spot.location = "560 Drillfield Dr, Blacksburg, VA"

        ReviewDB.create_review(starRating = 4, noiseLevel = 7, content = "Test content", crowdedness = 7, user = user, spot = spot)
        cursor.execute("SELECT * FROM spot_reviews;")
        result = cursor.fetchall()
        expected = [(1, 4, 7, "Test content", 7, 1, 1)]
        self.assertEqual(result, expected)

        cursor.close()
        db.close()

    def test_edit_spot_name(self):

        # Edit the name of a study spot
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        print("4. Editing a spot's name")
        SpotDB.edit_spot_name("Newman", "Newman Library")

        cursor.execute("SELECT * FROM study_spots;")
        result = cursor.fetchall()
        expected = [(1, "Newman", "560 Drillfield Dr, Blacksburg, VA")]
        self.assertEqual(result, expected)


        cursor.close()
        db.close()

    def test_edit_spot_location(self):

        # Edit the name of a study spot
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        print("4. Editing a spot's name")

        SpotDB.edit_spot_location("570 Drillfield Dr, Blacksburg, VA", "560 Drillfield Dr, Blacksburg, VA")

        cursor.execute("SELECT * FROM study_spots;")
        result = cursor.fetchall()
        expected = [(1, "Newman", "570 Drillfield Dr, Blacksburg, VA")]
        self.assertEqual(result, expected)


        cursor.close()
        db.close()
        

if __name__ == "__main__":
    unittest.main()
