from dataclasses import dataclass


@dataclass(frozen=True)
class Codecast:
    title: str
    publication_date: str

