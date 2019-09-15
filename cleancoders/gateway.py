from abc import ABC, abstractmethod
from typing import List, Optional

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.user import User


class Gateway(ABC):
    @abstractmethod
    def find_all_codecasts(self) -> List[Codecast]:
        pass

    @abstractmethod
    def delete(self, codecast: Codecast) -> None:
        pass

    @abstractmethod
    def save_codecast(self, codecast: Codecast) -> None:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass

    @abstractmethod
    def find_user(self, username: str) -> Optional[User]:
        pass
