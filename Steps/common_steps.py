import time

from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u': User is on the Login page')
def step_impl(context):
    context.driver.get("http://in-ka-wag1np:9999/index.php?loggedout")
    time.sleep(2)

@when(u': Clicks on Login Button')
def step_impl(context):
    context.Login = context.driver.find_element(By.ID,"loginButton")
    context.Login.click()
    time.sleep(2)


    context.title = context.driver.title


