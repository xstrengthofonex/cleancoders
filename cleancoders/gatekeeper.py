from typing import Optional

from cleancoders.entities.user import User


class Gatekeeper:
    def __init__(self):
        self.logged_in_user: Optional[User] = None

    def set_logged_in_user(self, user: User) -> None:
        self.logged_in_user = user

    def get_logged_in_user(self) -> Optional[User]:
        return self.logged_in_user
