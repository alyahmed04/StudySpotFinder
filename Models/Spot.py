from dataclasses import dataclass
import User

@dataclass
class Spot:

    name: str
    location: float
    noiseLevel: int
    content: str
    crowdedness: int
    user: User