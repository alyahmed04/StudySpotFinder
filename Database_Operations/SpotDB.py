from Models.Spot import Spot
from Database_Operations.ExecuteDB import execute_DBOperation


#Learned from the following sources about sql and mysqlconnector
#https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
#https://www.w3schools.com/python/python_mysql_update.asp
#https://www.red-gate.com/simple-talk/databases/mysql/modifying-mysql-data-from-within-python/


create_spot = ("INSERT INTO study_spots "
                "(spotName, location) "
                "VALUES (%s, %s)")
edit_spot_name = "UPDATE study_spots SET spotName = %s WHERE spotID = %s"
edit_spot_location = "UPDATE study_spots SET location = %s WHERE spotID = %s"
delete_spot = "DELETE FROM study_spots WHERE spotID = %s"

class SpotDB:

    def create_spot(spotName: str, location: str):
        value = (spotName, location)
        execute_DBOperation(create_spot, value)
        
    def edit_spot_name(spot: Spot, spotName: str):
        spot.spotName = spotName
        value = (spotName, spot.spotID)
        execute_DBOperation(edit_spot_name, value)

    def edit_spot_location(spot: Spot, location: str):

        spot.location = location
        value = (location, spot.spotID)
        execute_DBOperation(edit_spot_location, value)

    def delete_spot(spot: Spot):
        value = (spot.spotID,)
        execute_DBOperation(delete_spot, value)

