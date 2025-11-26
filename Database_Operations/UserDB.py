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
update_kudos = "UPDATE users SET kudos = %s WHERE userID = %s"
delete_user = "DELETE FROM users WHERE userID = %s"

class UserDB:


    #This function creates a user in the database
    def create_user(username: str, email: str, password: str, favoriteStudySpot: str, kudos: int = 0, spot: Spot = None):
        if spot is None:
            value = (username, email, password, spot, kudos)
        else:
            value = (username, email, password, spot.spotID, kudos)
        execute_DBOperation(create_user, value)


    #This function edits a users username in the database
    def edit_username(user: User, username: str):
        value = (username, user.userID)
        execute_DBOperation(edit_username, value)

    #This function edits a users favorite study spot in the database
    def edit_favorite_study_spot(user: User, spot: Spot):
        value = (spot.spotID, user.userID)
        execute_DBOperation(edit_favoriteStudySpot, value)
    
    #This function updates the kudos of the user by passing in the updated number of kudos
    def update_kudos(user: User, count: int):
        value = (count, user.userID)
        execute_DBOperation(update_kudos, value)

    #This function removes users from the database based on their userId
    def delete_user(user: User):
        value = (user.userID,)
        execute_DBOperation(delete_user, value)