import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from behave import *


@given(u': user is logged in')
def step_impl(context):
    context.driver = webdriver.Chrome()
    time.sleep(2)

    context.driver.get("http://localhost:9999/index.php?loggedout")
    time.sleep(4)
    context.username = context.driver.find_element(By.ID, "username")
    context.username.send_keys("nagesh")
    context.password = context.driver.find_element(By.ID, "password")
    context.password.send_keys("Alpha122@")
    time.sleep(2)
    context.Login = context.driver.find_element(By.ID, "loginButton")
    context.Login.click()
    time.sleep(2)




@when(u': user click on Infra Tab')
def step_impl(context):
    infra = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonConfig-button']"))
    )
    infra.click()



@when(u': User click on License Info')
def step_impl(context):
    licens_info = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='License Info']"))
    )

    licens_info.click()


@then(u': User should be validate for Valid License')
def step_impl(context):
    try:
        print("DEBUG: Starting license validation step")
        sys.stdout.flush()

        valid_license = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//td[contains(., 'HEADS UP: Your Uptime license will expire in')]"))
        )
        print("DEBUG: Element located successfully")
        sys.stdout.flush()


        lic = valid_license.text.strip()
        print(f"DEBUG: Before extraction check - lic: '{lic}'")
        sys.stdout.flush()
    finally:
        print("Finally bock")