from Actions.Perform_Driver_Action import perform_click, perform_find_element, perform_find_elements, perform_send_keys, perform_wait
from Data.Dynamic_Data import dynamic_data, dynamic_url
from Data.Queries import queries
from Data.Static_Data import static_data
from Database.Database import connect_and_run_query
from Locators.forgot_password_locators import forgot_password_locators, reset_password_locators
from Locators.login_locators import login_locators
from Pages.login_page import click_forgot_password_cta, enter_email
from Utils.Utils import get_data_from_webelement


def click_send_code_cta(driver):
    send_code_cta = perform_find_element(driver, "xpath", forgot_password_locators.send_code_cta)
    perform_click(driver, send_code_cta)

def enter_code(driver):
    code_fields = perform_find_elements(driver, "xpath", forgot_password_locators.code_fields)
    otp_digits = get_otp()
    if otp_digits == ['N', 'o', 'n', 'e']:
        print("DB is not connected")
        driver.close()
    else:
        for index, code_field in enumerate(code_fields):
            if index < len(otp_digits):
                perform_send_keys(code_field, otp_digits[index])
            else:
                print("Issue in entering OTP")

def get_otp():
    otp = connect_and_run_query(queries.get_otp_query)
    print(f"OTP from DB is : {otp}")
    otp_digits = list(str(otp))
    return otp_digits

def click_verify_cta(driver):
    verify_cta = perform_find_element(driver, "xpath", forgot_password_locators.verify_cta)
    perform_click(driver, verify_cta)

def click_reset_cta(driver):
    reset_cta = perform_find_element(driver, "xpath", reset_password_locators.reset_cta)
    perform_click(driver, reset_cta)

def enter_new_password(driver):
    password_field = perform_find_element(driver, "id", login_locators.password_field)
    perform_send_keys(password_field, dynamic_data.new_password)
    print(f"New Password entered : {get_data_from_webelement(password_field)}")
    confirm_password_field = perform_find_element(driver, "id", reset_password_locators.confirm_password_field)
    perform_send_keys(confirm_password_field, dynamic_data.new_password)
    print(f"Confirm Password entered : {get_data_from_webelement(confirm_password_field)}")
    if get_data_from_webelement(password_field) == get_data_from_webelement(confirm_password_field):
        click_reset_cta(driver)
        print("New password is set")
    else:
        print("Password and Confirm Password need to be same.")

def test_forgot_password(driver):
    click_forgot_password_cta(driver)
    perform_wait(driver, expected_url=f"{static_data.url+dynamic_url.forgot_password}")
    enter_email(driver)
    click_send_code_cta(driver)
    enter_code(driver)
    click_verify_cta(driver)
    enter_new_password(driver)
    
