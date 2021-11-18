from behave import *
from TDD_test import *

@given(
    "I have pistons for 120 dollars and cylinders for 100 dollars")
def have_prices(context):
    context.a = TestPartCost()


@when("I put them into engine")
def engine_combine(context):
    context.a.test_part_cost_is_working()


@then("I expect engine to cost 220 dollars")
def check_result(context):
    pass
