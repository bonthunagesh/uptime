import logging
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


logging.basicConfig(
    filename='logs_file.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)


@given(u': user is logged in and navigates to Test Configuration')
def step_impl(context):
    try:

        context.driver = webdriver.Chrome()
        time.sleep(2)


        context.driver.get("http://localhost:9999/index.php?loggedout")
        time.sleep(4)
        context.username = context.driver.find_element(By.ID, "username")
        context.username.send_keys("nagesh")
        context.password = context.driver.find_element(By.ID, "password")
        context.password.send_keys("Alpha122@")
        time.sleep(2)
        context.login = context.driver.find_element(By.ID, "loginButton")
        context.login.click()
        time.sleep(2)

        infra = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonConfig-button']"))
        )

        infra.click()

        auth = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='User Authentication']"))
        )

        auth.click()


    finally:

        time.sleep(2)


@when(u': User enters valid username and password')
def step_impl(context):
    try:

        uname = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='test_username']"))
        )
        uname.send_keys("admin")

        pwd = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='test_password']"))
        )
        pwd.send_keys("password")

        test_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='testConfiguration_runCommandButton']"))
        )
        test_button.click()

    except Exception as e:
        print(f"ERROR: Failed to enter credentials or click button: {e}")


@then(u': Success is seen')
def step_impl(context):
    logging.info("Inside then step")
    try:
        message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@id='testConfiguration_runCommandResult']//div[2][@class='info']"))
        )

        status = message.text.strip()

        logging.info(f"Actual status: '{status}'")

        assert "Skipping test, the admin user is always authenticated against the Uptime Data Stor" in status, f"Expected 'Success' message, but got '{status}'"

    except Exception as e:
        print(f"Failed to verify Success message: {e}")
        raise
