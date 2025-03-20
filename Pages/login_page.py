from Actions.Perform_Driver_Action import perform_click, perform_find_element, perform_send_keys
from Data.Dynamic_Data import dynamic_url
from Data.Static_Data import static_data
from Locators.login_locators import login_locators
from Utils.Utils import get_current_url, get_data_from_webelement, take_full_screenshot



def enter_username(driver):
    email_field = perform_find_element(driver, "id", login_locators.email_field)
    perform_send_keys(email_field, static_data.email)
    print(f"E-mail entered : {get_data_from_webelement(email_field)}")

def enter_password(driver):
    password_field = perform_find_element(driver, "id", login_locators.password_field)
    perform_send_keys(password_field, static_data.password)
    print(f"Password entered : {get_data_from_webelement(password_field)}")

def click_signin_cta(driver):
    signin_cta = perform_find_element(driver, "xpath", login_locators.sign_in_cta)
    perform_click(driver, signin_cta)

def validate_login(driver):
    expected_url = f"{static_data.url + dynamic_url.dashobard}"
    current_url = get_current_url(driver)
    if current_url == expected_url:
        print("Log in Done ")
    else:
        print("Issue with Log in")
        take_full_screenshot(driver)

def perform_login(driver):
    enter_username(driver)
    enter_password(driver)
    click_signin_cta(driver)
    validate_login(driver)

