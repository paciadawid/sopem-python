from behave import *
from hamcrest import *


@given("I have a unique user created")
def step_impl(context):
    context.gorest_handler.create_user()
    context.response_body, _ = context.gorest_handler.create_user()


@when("I update user using following data")
def step_impl(context):
    context.user_data = {}
    for row in context.table:
        context.user_data[row["key"]] = row["value"]

    context.response_body, status_code = context.gorest_handler.update_user(context.response_body["data"]["id"], context.user_data)
    assert_that(status_code, equal_to(200))


@then("I see user has a following data")
def step_impl(context):
    assert_that(context.response_body["data"], has_entries(context.user_data))
