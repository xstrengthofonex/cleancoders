from typing import List, Optional

from cleancoders.entities.codecast import Codecast
from cleancoders.gateway import Gateway
from cleancoders.entities.user import User


class MockGateway(Gateway):
    def __init__(self):
        self._codecasts: List[Codecast] = list()
        self._users: List[User] = list()

    def find_all_codecasts(self) -> List[Codecast]:
        return list(self._codecasts)

    def delete(self, codecast: Codecast) -> None:
        self._codecasts.remove(codecast)

    def save_codecast(self, codecast: Codecast) -> None:
        self._codecasts.append(codecast)

    def save_user(self, user: User) -> None:
        self._users.append(user)

    def find_user(self, username: str) -> Optional[User]:
        return next((u for u in self._users if u.username == username), None)
