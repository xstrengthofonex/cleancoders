from behave import given, when, step, then
from behave.runner import Context


@given("codecast")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: Given codecast')


@when("the user requests details for codecast episode-1")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: When the user requests details for codecast episode-1')


@then('the presented title is "{title}" published "{publication_date}"}')
def step_impl(context: Context, title: str, publication_date: str):
    raise NotImplementedError(u'STEP: Then the presented title is "A" published "3/01/2014')


@step("with option to purchase viewing license")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: And with option to purchase viewing license')


@step("with option to purchase download license")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: And with option to purchase download license')
