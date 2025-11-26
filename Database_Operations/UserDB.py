from Models.User import User
from Database_Operations.ExecuteDB import execute_DBOperation
from Models.Spot import Spot

#Learned from the following sources about sql and mysqlconnector
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
#https://www.w3schools.com/python/python_mysql_update.asp
#https://www.red-gate.com/simple-talk/databases/mysql/modifying-mysql-data-from-within-python/


create_user = ("INSERT INTO users "
                "(username, email, hashedPassword, favoriteStudySpot, kudos) "
                "VALUES (%s, %s, %s, %s, %s)")


edit_username = "UPDATE users SET username = %s WHERE userID = %s"
edit_favoriteStudySpot = "UPDATE users SET favoriteStudySpot = %s WHERE userID = %s"
delete_user = "DELETE FROM users WHERE userID = %s"

class UserDB:

    def create_user(username: str, email: str, password: str, favoriteStudySpot: Spot = None, kudos: int = 0):
        if favoriteStudySpot is None:
            value = (username, email, password, favoriteStudySpot, kudos)
        else:
            value = (username, email, password, favoriteStudySpot.spotID, kudos)
        execute_DBOperation(create_user, value)

    def edit_username(user: User, username: str):
        value = (username, user.userID)
        execute_DBOperation(edit_username, value)

    def edit_favorite_study_spot(user: User, spot: Spot):
        value = (spot.spotID, user.userID)
        execute_DBOperation(edit_favoriteStudySpot, value)

    def delete_user(user: User):
        #learned from:
        #https://stackoverflow.com/questions/61831138/creating-python-tuple-with-one-int-item
        value = tuple([user.userID,])
        
        execute_DBOperation(delete_user, value)