from dataclasses import dataclass

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.entity import Entity
from cleancoders.entities.user import User


@dataclass
class License(Entity):
    user: User
    codecast: Codecast
