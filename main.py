from Models.User import User
from Models.Spot import Spot
from Models.Review import Review
from Database_Operations.UserDB import UserDB
from Database_Operations.SpotDB import SpotDB
from Database_Operations.ReviewDB import ReviewDB

def test_create_studyspot():
    
    # Create a study spot
    print("1. Creating a study spot")
    SpotDB.create_spot("Newman Library", "560 Drillfield Dr, Blacksburg, VA")
    
def test_create_user():
    # Create a user
    print("2. Creating a user")
    UserDB.create_user(
        username="testuser5",
        email="test5@vt.edu",
        password="testPassword",
        favoriteStudySpot=None,
        kudos=0
    )

def test_create_review():
    print("3. Creating a review")
    # Not implemented yet

def test_edit_spot_name():

    # Edit the name of a study spot
    print("4. Editing a spot's name")
    SpotDB.edit_spot_name("Newman", "Newman Library")
    
if __name__ == "__main__":
    try:
        test_create_studyspot()
        print("\nStudy spot successfully created")
    except Exception as e:
        print(f"\nError occurred: {e}")

    try:
        test_create_user()
        print("\nUser successfully created")
    except Exception as e:
        print(f"\nError occurred: {e}")

    try:
        test_edit_spot_name()
        print("\nSpot name successfully edited")
    except Exception as e:
        print(f"\nError occurred: {e}")
