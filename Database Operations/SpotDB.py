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

create_spot = ("INSERT INTO study_spots "
                "(spotName, location) "
                "VALUES (%s, %s)")

#
edit_spot_name = "UPDATE study_spots SET spotName = %s WHERE spotID = %s"
edit_spot_location = "UPDATE study_spots SET location = %s WHERE spotID = %s"
delete_spot = "DELETE from study_spots WHERE spotID = %s"

cursor = db.cursor()

class SpotDB:

    def create_spot(spotName: str, location: str):
        value = (f"{spotName}", f"{location}")
        cursor.execute(create_spot, value)
        
    def edit_spot_name(spot: Spot, spotName: str):
        spot.spotName = spotName
        value = (f"{spotName}", f"{spot.spotID}")
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