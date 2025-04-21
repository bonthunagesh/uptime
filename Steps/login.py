import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u': user is logged')
def step_impl(context):
    context.driver = webdriver.Chrome()
    time.sleep(2)

    context.driver.get("http://localhost:9999/index.php?loggedout")
    time.sleep(4)


@when(u': user enters username and password')
def step_impl(context):

    context.username = context.driver.find_element(By.ID, "username")
    context.username.send_keys("nagesh")
    context.password = context.driver.find_element(By.ID, "password")
    context.password.send_keys("Alpha122@")
    time.sleep(2)
    context.Login = context.driver.find_element(By.ID, "loginButton")
    context.Login.click()
    time.sleep(2)



@then(u': user should be able to Log in to the application')
def step_impl(context):

    assert "My Portal" in context.driver.title, f"Expected 'Dashboard' in title, but got: {context.driver.title}"

    context.driver.quit()






