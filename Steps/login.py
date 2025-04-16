import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given(u': User is on the Login page')
def step_impl(context):
    context.driver.get("http://in-ka-wag1np:9999/index.php?loggedout")

@when(u': user enters username and password')
def step_impl(context):
    context.username = context.driver.find_element(By.ID, "username")
    context.username.send_keys("alex")

    time.sleep(2)

    context.password = context.driver.find_element(By.ID,"password")
    context.password.send_keys("password")
    time.sleep(2)


@when(u': Clicks on Login Button')
def step_impl(context):
    context.Login = context.driver.find_element(By.ID,"loginButton")
    context.Login.click()
    time.sleep(2)
    context.title = context.driver.title

@then(u': user should be able to Log in to the application')
def step_impl(context):
    time.sleep(2)

    assert "My Portal" in context.title, f"Expected 'Dashboard' in title, but got: {context.title}"






