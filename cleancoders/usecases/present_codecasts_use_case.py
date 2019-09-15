from dataclasses import dataclass
from typing import List

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
