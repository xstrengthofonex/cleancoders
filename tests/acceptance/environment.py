from behave.model import Scenario
from behave.runner import Context

from cleancoders.gatekeeper import Gatekeeper
from cleancoders.usecases.present_codecasts_use_case import PresentCodecastsUseCase
from cleancoders.mock_gateway import MockGateway


def before_scenario(context: Context, scenario: Scenario):
    context.gateway = MockGateway()
    context.gatekeeper = Gatekeeper()
    context.present_codecasts_usecase = PresentCodecastsUseCase(gateway=context.gateway)
