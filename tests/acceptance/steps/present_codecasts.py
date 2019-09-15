from behave import given, step, then
from behave.runner import Context


@given("no codecasts")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: Given no codecasts')


@given('user "{username}"')
def step_impl(context, username: str):
    raise NotImplementedError(u'STEP: Given user "U"')


@step('user "{username}" logged in')
def step_impl(context, username: str):
    raise NotImplementedError(u'STEP: And user "U" logged in')


@then('the following codecasts will be presented for "{username}"')
def step_impl(context, username: str):
    raise NotImplementedError(u'STEP: Then the following codecasts will be presented for "U"')


@step("there will be no codecasts presented")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: And there will be no codecasts presented')


@step("codecasts will be presented in chronological order")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: And codecasts will be presented in chronological order')


@given("codecasts")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: Given codecasts')


@step('with license for "{username}" able to download "{title}"')
def step_impl(context: Context, username: str, title: str):
    raise NotImplementedError(u'STEP: And with license for "U" able to download "A"')


@step('with license for "{username}" able to view "{title}"')
def step_impl(context: Context, username: str, title: str):
    raise NotImplementedError(u'STEP: And with license for "U" able to view "A"')
