import unittest

from cleancoders.usecases.present_codecasts_use_case import PresentCodecastsUseCase
from cleancoders.mock_gateway import MockGateway
from tests.builders import build_user, build_codecast, build_license


class PresentCodecastsUseCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.gateway = MockGateway()
        self.usecase = PresentCodecastsUseCase(gateway=self.gateway)
        self.user = self.get_saved_user()
        self.codecast = self.get_saved_codecast()

    def test_user_without_license_cannot_view_codecast(self):
        self.assertFalse(self.usecase.is_licensed_to_view(self.user, self.codecast))

    def test_user_with_view_license_can_view_codecast(self):
        view_license = build_license(user=self.user, codecast=self.codecast)
        self.gateway.save_license(view_license)
        self.assertTrue(self.usecase.is_licensed_to_view(self.user, self.codecast))

    def test_user_with_view_license_can_not_view_other_users_codecasts(self):
        other_user = build_user(username="Other User")
        view_license = build_license(user=self.user, codecast=self.codecast)
        self.gateway.save_license(view_license)
        self.assertFalse(self.usecase.is_licensed_to_view(other_user, self.codecast))

    def get_saved_codecast(self):
        return self.gateway.save_codecast(build_codecast())

    def get_saved_user(self):
        return self.gateway.save_user(build_user())
