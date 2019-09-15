from abc import ABC, abstractmethod
from typing import List, Optional

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.license import License
from cleancoders.entities.user import User


class Gateway(ABC):
    @abstractmethod
    def find_all_codecasts(self) -> List[Codecast]:
        pass

    @abstractmethod
    def delete(self, codecast: Codecast) -> None:
        pass

    @abstractmethod
    def save_codecast(self, codecast: Codecast) -> Codecast:
        pass

    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def save_license(self, license_: License) -> License:
        pass

    @abstractmethod
    def find_codecast_by_title(self, title: str) -> Optional[Codecast]:
        pass

    @abstractmethod
    def find_licenses_for(self, user: User, codecast: Codecast) -> List[License]:
        pass
