import time
import pdb

from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@when(u': user enters invalid_username and invalid_password')
def step_impl(context):
    wait = WebDriverWait(context.driver, 20)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))


@then(u': user should not be able to Log in to the application')
def step_impl(context):

    error_message = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid login credentials provided')]")
    time.sleep(2)
    if error_message.is_displayed():

        print("Validation passed: Error message displayed correctly.")


