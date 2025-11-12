from dataclasses import dataclass
import uuid

@dataclass
class Spot:

    spotID: uuid
    spotName: str
    location: float