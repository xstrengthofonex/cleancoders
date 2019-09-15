from cleancoders.entities.codecast import Codecast
from cleancoders.entities.license import License
from cleancoders.entities.user import User


def build_codecast(**params) -> Codecast:
    return Codecast(
        id=params.get("id", None),
        title=params.get("title", "Codecast"),
        publication_date=params.get("publication_date", "today"))


def build_user(**params) -> User:
    return User(
        id=params.get("id", None),
        username=params.get("username", "User"))


def build_license(**params) -> License:
    return License(
        user=params.get("user", build_user()),
        codecast=params.get("codecast", build_codecast()))
