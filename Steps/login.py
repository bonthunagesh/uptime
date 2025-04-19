import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



@when(u': user enters username and password')
def step_impl(context):
    context.username = context.driver.find_element(By.ID, "username")
    context.username.send_keys("nagesh")

    time.sleep(2)

    context.password = context.driver.find_element(By.ID,"password")
    context.password.send_keys("Alpha122@")
    time.sleep(2)

    try:
        ok_button = context.driver.find_element(By.XPATH, "//button[text()='OK']")
        ok_button.click()
        print("Popup closed successfully.")
    except Exception as e:
        print(f"Error closing popup: {e}")




@then(u': user should be able to Log in to the application')
def step_impl(context):
    time.sleep(2)

    assert "My Portal" in context.title, f"Expected 'Dashboard' in title, but got: {context.title}"

    context.driver.quit()






