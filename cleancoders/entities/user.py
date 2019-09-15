from dataclasses import dataclass

from cleancoders.entities.entity import Entity


@dataclass
class User(Entity):
    username: str
