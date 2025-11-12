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

# create_review = ("INSERT INTO review "
#                "(spot_Id, location, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")

create_spot = ("INSERT INTO studySpots "
                "(Id, name, location) "
                "VALUES (%s, %s, %s, %s, %s)")

#
edit_spot_name = "UPDATE spot SET spotName = %s WHERE spotId = %s"
edit_spot_location = "UPDATE spot SET location = %s WHERE spotID = %s"
delete_spot = "DELETE from studySpots WHERE spotID = %s"

cursor = db.cursor()

class SpotDB:

    def create_spot(spot: Spot):
        spot_id = uuid.uuid4()
        value = (f"{spot_id}", f"{spot.name}", f"{spot.location}")
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
        cursor.execute(delete_spot)

db.commit()
db.close()