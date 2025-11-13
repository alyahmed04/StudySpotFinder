from dataclasses import dataclass
import Spot

@dataclass
class User:

    userID: int
    username: str
    email: str
    password: str
    favoriteStudySpot: int
    kudos: int
    spot: Spot

    

