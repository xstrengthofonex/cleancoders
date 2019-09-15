from typing import List, Optional, cast
from uuid import uuid4

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.entity import Entity
from cleancoders.entities.license import License
from cleancoders.gateway import Gateway
from cleancoders.entities.user import User


class MockGateway(Gateway):
    def __init__(self):
        self._codecasts: List[Codecast] = list()
        self._users: List[User] = list()
        self._licenses: List[License] = list()

    def find_all_codecasts(self) -> List[Codecast]:
        return list(self._codecasts)

    def delete(self, codecast: Codecast) -> None:
        self._codecasts.remove(codecast)

    def save_codecast(self, codecast: Codecast) -> Codecast:
        self.establish_id(codecast)
        self._codecasts.append(codecast)
        return codecast

    def save_user(self, user: User) -> User:
        self.establish_id(user)
        self._users.append(user)
        return user

    def find_user(self, username: str) -> Optional[User]:
        return next((u for u in self._users if u.username == username), None)

    def save_license(self, license_: License) -> License:
        self._licenses.append(license_)
        return license_

    def find_codecast_by_title(self, title: str) -> Optional[Codecast]:
        return next((c for c in self._codecasts if c.title == title), None)

    def find_licenses_for(self, user: User, codecast: Codecast) -> List[License]:
        return [l for l in self._licenses
                if l.user == user and l.codecast == codecast]

    def establish_id(self, entity: Entity) -> None:
        if not entity.id:
            entity.id = self.get_next_id()

    @staticmethod
    def get_next_id() -> str:
        return str(uuid4())
