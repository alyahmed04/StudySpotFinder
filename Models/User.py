from dataclasses import dataclass
import Spot

@dataclass
class User:

    username: str
    email: str
    password: str
    favoriteStudySpot: str
    kudos: int
    spot: Spot

    

