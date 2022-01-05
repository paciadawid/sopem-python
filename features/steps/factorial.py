from behave import *
from hamcrest import *


@when("I calculate factorial {input}")
def step_impl(context, input):
    context.result = context.calculator.factorial_loop(int(input))


@then("I see the result {result}")
def step_impl(context, result):
    assert_that(context.result, equal_to(int(result)))
