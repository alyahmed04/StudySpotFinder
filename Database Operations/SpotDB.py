import mysql.connector
from Models.Spot import Spot
import uuid

config = {
  'user': 'placeholder',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'studyspot',
  'raise_on_warnings': True
}

db = mysql.connector.connect(**config)

create_spot = ("INSERT INTO studySpots "
                "(name, location) "
                "VALUES (%s, %s)")

#
edit_spot_name = "UPDATE spot SET spotName = %s WHERE spotID = %s"
edit_spot_location = "UPDATE spot SET location = %s WHERE spotID = %s"
delete_spot = "DELETE from studySpots WHERE spotID = %s"

cursor = db.cursor()

class SpotDB:

    def create_spot(name: str, location: str):
        value = (f"{name}", f"{location}")
        cursor.execute(create_spot, value)
        
    def edit_spot_name(spot: Spot, name: str):
        spot.name = name
        value = (f"{name}", f"{spot.spotID}")
        cursor.execute(edit_spot_name, value)

    def edit_spot_location(spot: Spot, location: str):

        spot.location = location
        value = (f"{location}", f"{spot.spotID}")
        cursor.execute(edit_spot_location, value)

    def delete_spot(spot: Spot):
        value = f"{spot.spotID}"
        cursor.execute(delete_spot, value)

db.commit()
db.close()