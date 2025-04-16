import time
import pdb

from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given(u': user is logged into the Application')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given : user is logged into the Application')


@when(u': user click on the Dashboards')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : user click on the Dashboards')


@then(u': Dashbaords page open')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Dashbaords page open')


@when(u': user click on My_portal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : user click on My_portal')


@then(u': My_portal page opens')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : My_portal page opens')


@when(u': User clicks on Infrastructure')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : User clicks on Infrastructure')


@then(u': Infrastructure page opens')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Infrastructure page opens')


@when(u': User click on Services Tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : User click on Services Tab')


@then(u': Services page  open')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Services page  open')


@when(u': User clicks on Reports tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : User clicks on Reports tab')


@then(u': Reports page opens')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Reports page opens')


@when(u': User clicks on Config tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : User clicks on Config tab')


@then(u': Config page open')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Config page open')


@when(u': user click on Syslist Tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : user click on Syslist Tab')


@then(u': Syslist page opens')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then : Syslist page opens')
