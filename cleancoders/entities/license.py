from dataclasses import dataclass

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.user import User


@dataclass
class License:
    user: User
    codecast: Codecast
