import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow INFO and WARNING

from behave import given, when, then

# Given: user is logged into the Application
@given(u': user is logged into the Application')
def step_impl(context):

    context.driver = webdriver.Chrome()
    time.sleep(4)

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



# When: user clicks on Dashboards
@when(u': user click on the Dashboards')
def step_impl(context):
    Dashboard = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonDashboards-button']"))
    )
    Dashboard.click()

# Then: Dashboards page opens
@then(u': Dashboards page open')
def step_impl(context):
    try:
        assert "Uptime: Dashboards" in context.driver.title, f"Expected 'Uptime: Dashboards' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Dashboards page check failed: {e}")

# When: user clicks on My_portal
@when(u': user click on My_portal')
def step_impl(context):
    my_portal = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonMyPortal-button']"))
    )
    my_portal.click()

# Then: My_portal page opens
@then(u': My_portal page opens')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] My Portal page check failed: {e}")

# When: user clicks on Infrastructure
@when(u': User clicks on Infrastructure')
def step_impl(context):
    infra = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonMyInfrastructure-button']"))
    )
    infra.click()

# Then: Infrastructure page opens
@then(u': Infrastructure page opens')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Infrastructure page check failed: {e}")

# When: user clicks on Services Tab
@when(u': User click on Services Tab')
def step_impl(context):
    services = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonServices-button']"))
    )
    services.click()

# Then: Services page open
@then(u': Services page open')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Services page check failed: {e}")

# When: user clicks on Reports tab
@when(u': User clicks on Reports tab')
def step_impl(context):
    Reports = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonReports-button']"))
    )
    Reports.click()

# Then: Reports page opens
@then(u': Reports page opens')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Reports page check failed: {e}")

# When: user clicks on Config tab
@when(u': User clicks on Config tab')
def step_impl(context):
    config = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonConfig-button']"))
    )
    config.click()

# Then: Config page open
@then(u': Config page open')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Config page check failed: {e}")

# When: user clicks on Syslist Tab
@when(u': user click on Syslist Tab')
def step_impl(context):
    syslist = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='buttonSyslist-button']"))
    )
    syslist.click()

# Then: Syslist page opens
@then(u': Syslist page opens')
def step_impl(context):
    try:
        assert "My Portal" in context.driver.title, f"Expected 'My Portal' in title, but got: {context.driver.title}"
    except Exception as e:
        print(f"[FAIL] Syslist page check failed: {e}")
    context.driver.quit()