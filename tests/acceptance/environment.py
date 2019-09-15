from behave.model import Scenario
from behave.runner import Context

from cleancoders.gatekeeper import Gatekeeper
from tests.unit.mock_gateway import MockGateway


def before_scenario(context: Context, scenario: Scenario):
    context.gateway = MockGateway()
    context.gatekeeper = Gatekeeper()


