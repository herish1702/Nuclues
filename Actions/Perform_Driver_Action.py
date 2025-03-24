from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def perform_click(driver, webelement):
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(webelement)).click()

def perform_send_keys(webelement, data):
    webelement.send_keys(data)

def perform_find_element(driver, locator_type, locator_value):
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((getattr(By, locator_type.upper()), locator_value)))
    return driver.find_element(getattr(By, locator_type.upper()), locator_value)

def perform_find_elements(driver,locator_type, locator_value):
    WebDriverWait(driver,60).until(EC.visibility_of_element_located((getattr(By, locator_type.upper()), locator_value)))
    return driver.find_elements(getattr(By, locator_type.upper()), locator_value)

def perform_wait(driver, expected_url=None, webelement=None, timeout=60):
    if expected_url:
        WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
    elif webelement:
        WebDriverWait(driver, timeout).until(EC.visibility_of(webelement))
    else:
        print("Timeout issue")