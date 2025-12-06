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

#learned about unit test order from 
#https://stackoverflow.com/questions/4095319/unittest-tests-order

#SQL commands and sql connector learned from under various pages
#https://www.w3schools.com/python/python_mysql_where.asp
#https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchone.html
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html


class test_SQL_commands(unittest.TestCase):        

    #This method tests the creation of study spot in the SpotDB class
    def test_01_create_studyspot(self):

        # Create a study spot
        print("1. Creating a study spot")
        SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Newman Library'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()


        #expected tuple from query
        expected = (1, "Newman Library", "560 Drillfield Dr, Blacksburg, VA")
        self.assertEqual(result[1], expected[1])
        self.assertEqual(result[2], expected[2])

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM study_spots WHERE spotName = 'Newman Library'")

        db.commit()
        cursor.close()
        db.close()


    #This method tests the creation of a user in the UserDB class
    def test_02_create_user(self):


        # Create a user
        print("2. Creating a user")
        UserDB.create_user(
            username="testuser5",
            email="test5@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
        )

        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'testuser5'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        #expected tuple from query
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


    #This method tests the creation of a review in the ReviewDB class
    def test_03_create_review(self):


        print("3. Creating a review")
        
        #create a user to bind to a review
        UserDB.create_user(
            username="testuser2",
            email="test2@vt.edu",
            password="testPassword",
            favoriteStudySpot=None, 
            kudos=0
        )

        #create a study spot to bind to a review
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

 
        #Syntax for and learned from:
        #https://stackoverflow.com/questions/69960814/how-to-use-where-and-in-mysql-query-and-python
        cursor.execute("SELECT * FROM spot_reviews WHERE userID = %s AND spotID = %s", (userRes[0], spotRes[0]))

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        #Create the expected tuple from query
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


    #This method tests the edit of a study spots name in the SpotDB class
    def test_04_edit_spot_name(self):

        print("4. Editing a spot's name")

         # Create a new study spot
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

        # Edit the name of a study spot
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


    #This method tests the edit of a study spots location in the SpotDB class
    def test_05_edit_spot_location(self):
       
        print("5. Editing a spot's location")

        # Create new a study spot
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

        # Edit the study spot's Location
        SpotDB.edit_spot_location(spot, "570 Drillfield Dr, Blacksburg, VA")
        
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'man'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        result = cursor.fetchone()

        #expected tuple from query
        expected = (spotRes[0], "man", "570 Drillfield Dr, Blacksburg, VA")
        self.assertEqual(result, expected)

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM study_spots WHERE spotName = 'man'")
        
        db.commit()

        cursor.close()
        db.close()
    

    #This method tests the edit of a user's username in the UserDB class
    def test_06_edit_username(self):
        
        print("6. Edit a user's username")
        
        #Create a new user
        UserDB.create_user(
            username="testuser3",
            email="test3@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
        )

        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'testuser3'")
        
        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        userRes = cursor.fetchone()

       
        user = User(userID=userRes[0], username="testuser3",email="test3@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0) 

        cursor.close()
        db.close()

        #Edit the user's username
        UserDB.edit_username(user, "EditUserNameTest")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        #learned from:
        #https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
        value = tuple([userRes[0],])

        cursor.execute("SELECT * FROM users WHERE userID = %s", value)

        result = cursor.fetchone()

        #Expeted tuple from query
        expected = (userRes[0], "EditUserNameTest", "test3@vt.edu", "testPassword", None, 0)
        
        self.assertEqual(result, expected)
        
        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM users WHERE userID = %s", value)

        db.commit()

        cursor.close()
        db.close()
    

    #This method tests the edit of a user's favorite study spot in the UserDB class
    def test_07_edit_favorite_spot(self):

        print("7. Edit Favorite Spot")
        
        #Create a new user
        UserDB.create_user(
            username="testuser4",
            email="test4@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
        )

        #Create a new study spot
        SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Newman Library'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        spotRes = cursor.fetchone()

        spot = Spot(spotID=spotRes[0],spotName="Newman Library",location="560 Drillfield Dr, Blacksburg, VA")

        cursor.execute("SELECT * FROM users WHERE username = 'testuser4'")
        
        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        userRes = cursor.fetchone()

       
        user = User(userID=userRes[0], username="testuser4",email="test4@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0) 

        cursor.close()
        db.close()

        #Edit the users favorite study spot
        UserDB.edit_favorite_study_spot(user, spot)

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        #learned from:
        #https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
        userId = tuple([userRes[0],])
        spotId = tuple([spotRes[0],])


        cursor.execute("SELECT * FROM users WHERE userID = %s", userId)

        result = cursor.fetchone()

        #Expected tuple from query
        expected = (userRes[0], "testuser4", "test4@vt.edu", "testPassword", spotRes[0], 0)
        
        self.assertEqual(result, expected)
        

        #learned from:
        #https://www.w3schools.com/python/python_mysql_delete.asp
        cursor.execute("DELETE FROM users WHERE userID = %s", userId)
        cursor.execute("DELETE FROM study_spots WHERE spotID = %s", spotId)

        db.commit()

        cursor.close()
        db.close()
    

     #This method tests the removal of a user in the UserDB class
    def test_08_remove_user(self):

        print("8. Remove User")

        #Create a new user
        UserDB.create_user(
            username="testuser6",
            email="test6@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
        )

        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'testuser6'")
        
        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        userRes = cursor.fetchone()
        user = User(userID=userRes[0], username="testuser6",email="test6@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0) 

        cursor.close()
        db.close()

        #Remove the user
        UserDB.delete_user(user)

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = 'testuser6'")

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        removedUserRes = cursor.fetchone()

        self.assertIsNone(removedUserRes)

        cursor.close()
        db.close()
    

    #This method tests the removal of a study spot in the SpotDB class
    def test_09_remove_spot(self):

        print("9. Remove Study Spot")

        #Create a new study spot
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

        #Remove the study spot
        SpotDB.delete_spot(spot)

        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        #learned from:
        #https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
        spotId = tuple([spotRes[0],])

        cursor.execute("SELECT * FROM study_spots WHERE spotID = %s", spotId)

        #learned from:
        #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
        removedSpotRes = cursor.fetchone()

        self.assertIsNone(removedSpotRes)

        cursor.close()
        db.close()


    #This method tests to ensure that invalid input for spot creation are handled properly and logically.     
    def test_10_invalid_cases(self):
        print("10: Testing invalid inputs and cases")
        # Attempt to create a study spot with invalid name
        with self.assertRaises(Exception):
            #attempt to create spot with empty name (not NULL empty string)
            SpotDB.create_spot("", "24060 Kent St, Blacksburg, VA")
        with self.assertRaises(Exception):
            #attempt to create spot with NULL name
            SpotDB.create_spot(None, "24060 Kent St, Blacksburg, VA")
        # Attempt to create a spot with an invalid location
        with self.assertRaises(Exception):
            #attempt to create spot with empty location (not NULL empty string)
            SpotDB.create_spot("Test Spot", "")
        with self.assertRaises(Exception):
            #attempt to create spot with NULL location
            SpotDB.create_spot("Test Spot", None)


    #This method tests that deleting a study spot will delete all reviews associated with it via cascade deletion
    def test_11_integration_cascade_deletion(self):

        print("11. Integration Cascade Deletion Test")
        
        try:

            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            #Create a new user
            UserDB.create_user(
                username="testuser11",
                email="test11@vt.edu",
                password="testPassword",
                favoriteStudySpot=None,
                kudos=0
            )

            cursor.execute("SELECT * FROM users WHERE username = 'testuser11'")

            #learned from:
            #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
            userRes = cursor.fetchone()
            user = User(userID=userRes[0], username="testuser11",email="test11@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0)

            #Create a new study spot
            SpotDB.create_spot("Newman Library Test 11", "560 Drillfield Dr, Blacksburg, VA")

            cursor.close()
            db.close()
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Newman Library Test 11'")

            #learned from:
            #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
            spotRes = cursor.fetchone()
            spot = Spot(spotID=spotRes[0],spotName="Newman Library Test 11",location="560 Drillfield Dr, Blacksburg, VA")

            #Create a new review
            ReviewDB.create_review(
                starRating = 5,
                noiseLevel = 3,
                content = "Great place to study!",
                crowdedness = 4,
                user = user,
                spot = spot
            )

            cursor.close()
            db.close()
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM spot_reviews WHERE spotID = %s AND userID = %s",
                (spot.spotID, user.userID)
            )

            reviewCountBeforeDeletion = cursor.fetchone()[0]
            #Ensure that the review was created successfully
            self.assertEqual(reviewCountBeforeDeletion, 1)

            #Delete the study spot, which should cascade delete the review
            SpotDB.delete_spot(spot)

            # Close and reopen connection to see the cascade deletion
            cursor.close()
            db.close()
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM spot_reviews WHERE spotID = %s",
                (spot.spotID,)
            )

            reviewCountAfterDeletion = cursor.fetchone()[0]
            #Ensure that the review was deleted successfully via cascade deletion
            self.assertEqual(reviewCountAfterDeletion, 0)
             

            
        finally:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()
            #learned from:
            #https://www.w3schools.com/python/python_mysql_delete.asp
            cursor.execute("DELETE FROM users WHERE username = 'testuser11'")
            cursor.execute("DELETE FROM study_spots WHERE spotName = 'Newman Library Test 11'")

            db.commit()

            cursor.close()
            db.close()

    #This method tests editing all editable fields of a review in the ReviewDB class
    def test_12_edit_review_fields(self):
        print("12. Editing all fields in a review")
        try:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()
            #create a user for the review
            UserDB.create_user(
                username="testuser12",
                email="test12@vt.edu",
                password="testPassword",
                favoriteStudySpot=None, 
                kudos=0
            )

            #create a study spot for the review
            SpotDB.create_spot("New", "580 Drillfield Dr, Blacksburg, VA")

            cursor.close()
            db.close()
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute("SELECT * FROM users WHERE username = 'testuser12'")

            #learned from:
            #https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
            userRes = cursor.fetchone()
            user = User(userID=userRes[0],username="testuser12",email="test12@vt.edu",password="testPassword",favoriteStudySpot=None,kudos=0)

            cursor.execute("SELECT * FROM study_spots WHERE spotName = 'New'")

            spotRes = cursor.fetchone()
            spot = Spot(spotID=spotRes[0],spotName="New",location="580 Drillfield Dr, Blacksburg, VA")

            cursor.close()
            db.close()

            ReviewDB.create_review(starRating = 4, noiseLevel = 7, content = "Test content", crowdedness = 7, user = user, spot = spot)

            # Fetch the reviewID that was just inserted
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute(
                "SELECT * FROM spot_reviews WHERE userID = %s AND spotID = %s ORDER BY reviewID DESC LIMIT 1",
                (user.userID, spot.spotID)
            )

            reviewRes = cursor.fetchone()

            review = Review(
                reviewID=reviewRes[0],
                spot = spot,
                user = user,
                noiseLevel=reviewRes[3],
                crowdedness=reviewRes[4],
                starRating=reviewRes[5],
                content=reviewRes[6]
            )

            cursor.close()
            db.close()

            # --------------------------------------------------------
            # Perform edits on every field
            # --------------------------------------------------------
            ReviewDB.edit_review_rating(review, 5)
            ReviewDB.edit_review_text(review, "Updated text")
            ReviewDB.edit_review_noiseLevel(review, 4)
            ReviewDB.edit_review_crowdedness(review, 3)

            # --------------------------------------------------------
            # Fetch updated review to validate changes
            # --------------------------------------------------------
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            # Value needed for the SELECT statement
            value = tuple([review.reviewID,])

            cursor.execute("SELECT * FROM spot_reviews WHERE reviewID = %s", value)

            updated = cursor.fetchone()

            expected = (
                review.reviewID,
                spot.spotID,
                user.userID,
                4,   # noiseLevel updated
                3,   # crowdedness updated
                5, # starRating updated
                "Updated text"  # content updated
            )

            self.assertEqual(updated, expected)

        finally:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()
            # --------------------------------------------------------
            # Cleanup: Remove the review row
            # --------------------------------------------------------
            cursor.execute("DELETE FROM spot_reviews WHERE reviewID = %s", value)
            cursor.execute("DELETE FROM users WHERE username = 'testuser12'")
            cursor.execute("DELETE FROM study_spots WHERE spotName = 'New'")
            db.commit()

            cursor.close()
            db.close()



    #This method tests the removal of a review in the ReviewDB class
    def test_13_delete_review(self):

        print("13. Remove a review")
        try:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            UserDB.create_user(
            username="testuser_delete",
            email="testdelete@vt.edu",
            password="testPassword",
            favoriteStudySpot=None,
            kudos=0
            )

            SpotDB.create_spot("Delete Test Spot", "123 Test St, Blacksburg, VA")

            cursor.close()
            db.close()
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            cursor.execute("SELECT * FROM users WHERE username = 'testuser_delete'")
            userRes = cursor.fetchone()
            user = User(userID=userRes[0], username="testuser_delete", email="testdelete@vt.edu", password="testPassword", favoriteStudySpot=None, kudos=0)

            cursor.execute("SELECT * FROM study_spots WHERE spotName = 'Delete Test Spot'")
            spotRes = cursor.fetchone()
            spot = Spot(spotID=spotRes[0], spotName="Delete Test Spot", location="123 Test St, Blacksburg, VA")

            cursor.close()
            db.close()

            # --------------------------------------------------------
            # Insert a review to delete
            # --------------------------------------------------------
            ReviewDB.create_review(
                starRating=3,
                noiseLevel=2,
                content="Content to delete",
                crowdedness=1,
                user=user,
                spot=spot
            )

            # --------------------------------------------------------
            # Fetch the reviewID that was just inserted
            # --------------------------------------------------------
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            # Syntax learned from:
            # https://stackoverflow.com/questions/69960814/how-to-use-where-and-in-mysql-query-and-python
            cursor.execute(
                "SELECT * FROM spot_reviews WHERE userID = %s AND spotID = %s ORDER BY reviewID DESC LIMIT 1",
                (user.userID, spot.spotID)
            )

            reviewRes = cursor.fetchone()

            review = Review(
                reviewID=reviewRes[0],
                spot=spot,
                user=user,
                noiseLevel=reviewRes[3],
                crowdedness=reviewRes[4],
                starRating=reviewRes[5],
                content=reviewRes[6]
            )

            cursor.close()
            db.close()

            # --------------------------------------------------------
            # Perform the deletion
            # --------------------------------------------------------
            ReviewDB.delete_review(review)

            # --------------------------------------------------------
            # Fetch from DB to ensure the review was removed
            # --------------------------------------------------------
            db = mysql.connector.connect(**config)
            cursor = db.cursor()

            # Learn how to create single-item tuples:
            # https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
            value = tuple([review.reviewID,])

            cursor.execute("SELECT * FROM spot_reviews WHERE reviewID = %s", value)

            removedReviewRes = cursor.fetchone()

            # The review should no longer exist
            self.assertIsNone(removedReviewRes)

        finally:
            db = mysql.connector.connect(**config)
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE username = 'testuser_delete'")
            cursor.execute("DELETE FROM study_spots WHERE spotName = 'Delete Test Spot'")
            db.commit()
            cursor.close()
            db.close()


if __name__ == "__main__":
    unittest.main()