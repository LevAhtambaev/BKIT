from behave import *
from tests_tdd.tdd_test import *


@given('bot')
def first_step(context):
    context.a = TestBot()


@when('car_check return ok')
def check_sneakers(context):
    context.a.test_1()


@when('equipment_check return ok')
def check_slates(context):
    context.a.test_2()


@then('all is working good')
def last_step(context):
    pass