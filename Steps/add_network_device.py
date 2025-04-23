import time
from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import logging

logging.basicConfig(filename='Logs/Add_network_logsfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@given(u'user is logged in and navigates to My Infrastructure')
def step_user_is_logged_in_and_navigates_to_my_infrastructure(context):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get("http://localhost:9999/index.php?loggedout")
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        context.driver.find_element(By.ID, "username").send_keys("nagesh")
        context.driver.find_element(By.ID, "password").send_keys("Alpha122@")
        context.driver.find_element(By.ID, "loginButton").click()

        time.sleep(2)


        infraTab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"buttonMyInfrastructure")
        ))

        infraTab.click()

        time.sleep(2)

        logging.info("Navigated to My Infrastructure")

    except Exception as e:
        logging.error(f"Setup failed: {e}")
        context.driver.save_screenshot("HTML_reporting/given_error.png")
        raise

@when(u'user clicks Add System and fills the necessary details')
def step_user_clicks_add_system_and_fills_form(context):
    try:

        context.original_window = context.driver.current_window_handle
        logging.info(f"Original window handle: {context.original_window}")


        add_system_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add System/Network Device']"))
        )


        add_system_button.click()

        time.sleep(2)

        logging.info("Clicked Add System button")


        WebDriverWait(context.driver, 10).until(EC.number_of_windows_to_be(2))
        logging.info("New window detected")


        all_windows = context.driver.window_handles
        for window in all_windows:
            if window != context.original_window:
                context.driver.switch_to.window(window)
                break

        display_name = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "display_name"))
        )
        display_name.clear()
        display_name.send_keys("nagesh Localhost")

        time.sleep(2)

        Descr = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "description"))
        )

        Descr.send_keys("description")


        Host_name = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "value_[hostname]"))
        )
        Host_name.clear()
        time.sleep(1)

        Host_name.send_keys("Localhost")
        Host_name.clear()
        Host_name.send_keys("Localhost")

        time.sleep(4)

        save_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Save']"))
        )
        save_button.click()


    except Exception as e:
        logging.error(f"Failed during form filling: {e}")
        context.driver.save_screenshot("save_error.png")
        raise

@then(u'the system is added successfully')
def step_system_added_successfully(context):
    try:


        context.driver.switch_to.window(context.original_window)

        context.driver.refresh()
        time.sleep(5)

        system_added = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'nagesh Localhost (Localhost)')]"))
        )
        logging.info("Local Network Device found in the list")

        time.sleep(7)

    except Exception as e:
        logging.error(f"Validation failed: {e}")
        context.driver.save_screenshot("HTML_reporting/then_error.png")
        raise
