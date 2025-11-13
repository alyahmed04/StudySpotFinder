from dataclasses import dataclass
import Spot


#Learned dataclass from 
#https://docs.python.org/3/tutorial/classes.html
@dataclass
class User:

    userID: int
    username: str
    email: str
    password: str
    favoriteStudySpot: int
    kudos: int
    spot: Spot

    

