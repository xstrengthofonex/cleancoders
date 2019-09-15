from dataclasses import dataclass
from typing import List

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.user import User
from cleancoders.gateway import Gateway


@dataclass(frozen=True)
class PresentableCodecast:
    pass


class PresentCodecastsUseCase:
    def __init__(self, gateway: Gateway) -> None:
        self.gateway = gateway

    def present_codecasts(self, logged_in_user: User) -> List[PresentableCodecast]:
        return list()

    def is_licensed_to_view(self, user: User, codecast: Codecast) -> bool:
        licenses = self.gateway.find_licenses_for(user, codecast)
        return len(licenses) is not 0
