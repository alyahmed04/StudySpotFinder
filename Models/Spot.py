from dataclasses import dataclass

#Learned dataclass from 
#https://docs.python.org/3/tutorial/classes.html
@dataclass
class Spot:

    spotID: int
    spotName: str
    location: str