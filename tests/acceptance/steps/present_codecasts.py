from typing import List

from behave import given, step, then
from behave.runner import Context

from cleancoders.entities.codecast import Codecast
from cleancoders.entities.license import License
from cleancoders.entities.user import User


@given("no codecasts")
def step_impl(context: Context):
    codecasts: List[Codecast] = context.gateway.find_all_codecasts()
    for codecast in codecasts:
        context.gateway.delete(codecast)
    assert 0 == len(context.gateway.find_all_codecasts())


@given('user "{username}"')
def step_impl(context: Context, username: str):
    user = User(username=username)
    context.gateway.save_user(user)
    assert user == context.gateway.find_user(username)


@step('user "{username}" logged in')
def step_impl(context: Context, username: str):
    user = context.gateway.find_user(username)
    if user:
        context.gatekeeper.set_logged_in_user(user)


@then('the following codecasts will be presented for "{username}"')
def step_impl(context: Context, username: str):
    assert context.gatekeeper.get_logged_in_user() is not None


@step("there will be no codecasts presented")
def step_impl(context: Context):
    user = context.gatekeeper.get_logged_in_user()
    codecasts = context.present_codecasts_usecase.present_codecasts(user)
    assert 0 == len(codecasts)


@step("codecasts will be presented in chronological order")
def step_impl(context: Context):
    raise NotImplementedError(u'STEP: And codecasts will be presented in chronological order')


@given("codecasts")
def step_impl(context: Context):
    for row in context.table:
        codecast = Codecast(
            title=row.get("title", ""),
            publication_date=row.get("published", ""))
        context.gateway.save_codecast(codecast)


@step('with license for "{username}" able to download "{title}"')
def step_impl(context: Context, username: str, title: str):
    raise NotImplementedError(u'STEP: And with license for "U" able to download "A"')


@step('with license for "{username}" able to view "{title}"')
def step_impl(context: Context, username: str, title: str):
    user = context.gatekeeper.get_logged_in_user()
    codecast = context.gateway.find_codecast_by_title(title)
    license_ = License(user=user, codecast=codecast)
    context.gateway.save_license(license_)
    assert context.present_codecasts_usecase.is_licensed_to_view(user, codecast) is True

