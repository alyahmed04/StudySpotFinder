from dataclasses import dataclass
from Models import User
from Models import Spot


#Learned dataclass from 
#https://docs.python.org/3/tutorial/classes.html
@dataclass
class Review:

    reviewID: int
    starRating: int
    noiseLevel: int
    crowdedness: int
    content: str
    user: User
    spot: Spot
    