from dataclasses import dataclass
import User
import Spot


#Learned dataclass from 
#https://docs.python.org/3/tutorial/classes.html
@dataclass
class Review:

    reviewID: int
    rating: int
    noiseLevel: int
    content: str
    crowdedness: int
    user: User
    spot: Spot
    