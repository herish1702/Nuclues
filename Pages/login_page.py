from Actions.Perform_Driver_Action import perform_click, perform_find_element, perform_send_keys
from Data.Dynamic_Data import dynamic_data
from Data.Static_Data import static_data
from Locators.login_locators import login_locators
from Utils.Utils import clear_existing_data, get_data_from_webelement, take_full_screenshot



def enter_email(driver):
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

def click_forgot_password_cta(driver):
    forgot_password_cta = perform_find_element(driver, "xpath", login_locators.forgot_password_cta)
    perform_click(driver, forgot_password_cta)

def validate_login(driver):
    toaster_message = perform_find_element(driver, "xpath", login_locators.log_in_toaster_message)
    if toaster_message.is_displayed():
        print("Log in Done ")
    else:
        print("Issue with Log in")
        take_full_screenshot(driver)

def perform_login(driver):
    enter_email(driver)
    enter_password(driver)
    click_signin_cta(driver)
    validate_login(driver)



