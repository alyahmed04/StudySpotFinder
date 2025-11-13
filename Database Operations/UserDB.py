import mysql.connector
from Models.User import User
from ExecuteDB import execute_DBOperation
from Models.Spot import Spot

create_user = ("INSERT INTO users "
                "(username, email, hashedPassword, favoriteStudySpot, kudos) "
                "VALUES (%s, %s, %s, %s, %s)")

#
edit_username = "UPDATE users SET username = %s WHERE userID = %s"
edit_favoriteStudySpot = "UPDATE users SET favoriteStudySpot = %s WHERE userID = %s"
delete_user = "DELETE from users WHERE userID = %s"

class UserDB:

    def create_user(username: str, email: str, password: str, favoriteStudySpot: str, kudos: int = 0, spot: Spot = None):
        if spot is None:
            value = (username, email, password, spot, kudos)
        else:
            value = (username, email, password, spot.spotID, kudos)
        execute_DBOperation(create_user, value)

    # def compare_user_creditentials(user: User):
    #     db = mysql.connector.connect(**config)
    #     print("hello")
    #     print("hello")
    #     #sometjhng 
    #     db.close()

    def edit_username(user: User, username: str):
        value = (username, user.userID)
        execute_DBOperation(edit_username, value)


    def edit_favorite_study_spot(user: User, spot: Spot):
        value = (spot.spotID, user.userID)
        execute_DBOperation(edit_favoriteStudySpot, value)

    def delete_user(user: User):
        value = (user.userID,)
        execute_DBOperation(delete_user, value)