from dataclasses import dataclass
import User

@dataclass
class Review:

    username: str
    rating: float
    noiseLevel: int
    content: str
    crowdedness: int
    user: User
    