from dataclasses import dataclass
import User
import Spot

@dataclass
class Review:

    reviewID: int
    rating: int
    noiseLevel: int
    content: str
    crowdedness: int
    user: User
    spot: Spot
    