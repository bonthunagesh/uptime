import allure
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(
    filename='logs_file.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@given(u': user is logged in and navigates to Test Configuration')
@allure.step("Log in and navigate to Test Configuration")
def step_impl(context):
    try:
        context.driver = webdriver.Chrome()
        time.sleep(2)
        context.driver.get("http://localhost:9999/index.php?loggedout")
        time.sleep(4)

        context.driver.find_element(By.ID, "username").send_keys("nagesh")
        context.driver.find_element(By.ID, "password").send_keys("Alpha122@")
        context.driver.find_element(By.ID, "loginButton").click()
        time.sleep(2)

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'buttonConfig-button'))
        ).click()

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='User Authentication']"))
        ).click()

        allure.step("User successfully navigated to Test Configuration.")

    except Exception as e:
        logging.error(f"Setup failed: {e}")
        raise


@when(u'User enters valid "{username}" and "{password}"')
@allure.step("User enters valid credentials")
def step_impl(context, username, password):
    try:
        uname = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "test_username"))
        )
        uname.clear()
        uname.send_keys(username)

        pwd = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "test_password"))
        )
        pwd.clear()
        pwd.send_keys(password)

        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "testConfiguration_runCommandButton"))
        ).click()

        allure.step(f"Entered username: {username} and password: {password}")

    except Exception as e:
        logging.error(f"Failed during input: {e}")
        raise


@then(u'Success is seen with message {expected_message}')
def step_impl(context, expected_message):
    try:
        message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='testConfiguration_runCommandResult']//div[2][@class='info']"))
        )
        actual_text = message.text.strip()
        logging.info(f"Actual status: '{actual_text}'")


        if "passed." in actual_text.lower():
            logging.info("Validation passed: 'passed' found in the message")
        elif "failed." in actual_text.lower():
            logging.info("Validation failed: 'failed' found in the message")
            assert False, f"Test failed: 'failed' detected in '{actual_text}'"
        else:
            logging.warning(f"Validation unclear: Neither 'passed' nor 'failed' found in '{actual_text}'")
            assert False, "Unable to determine test status"

    except Exception as e:
        logging.error(f"Validation failed: {e}")
        context.driver.save_screenshot("HTML_reporting/error.png")
        raise
    finally:
        if hasattr(context, 'driver') and context.driver:
            context.driver.quit()
