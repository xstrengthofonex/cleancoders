from dataclasses import dataclass

from cleancoders.entities.entity import Entity


@dataclass
class Codecast(Entity):
    title: str
    publication_date: str

