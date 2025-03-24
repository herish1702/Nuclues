from Actions.Perform_Driver_Action import perform_click, perform_find_element, perform_send_keys
from Data.Dynamic_Data import dynamic_data
from Locators.tenant_locators import tenant_locators,create_new_tenant_locators
from Pages.navbar_page import click_tenant
from Utils.Utils import move_to_element_and_send, perform_scroll_to

def add_new_tenant(driver):
    click_tenant(driver)
    click_add_tenant_cta(driver)
    enter_tenant_name(driver)
    enter_prefix(driver)
    enter_company_name(driver)
    enter_email(driver)
    enter_address(driver)
    enter_flat_details(driver)
    # enter_country(driver)
    # enter_state(driver)
    add_zip_code(driver)
    # enter_status(driver)
    add_company_profile(driver)

def click_add_tenant_cta(driver):
    add_tenant_cta = perform_find_element(driver, "xpath",tenant_locators.add_tenant_cta)
    perform_click(driver, add_tenant_cta)

def enter_tenant_name(driver):
    tenant_name_field = perform_find_element(driver, "xpath", create_new_tenant_locators.tenant_name)
    perform_send_keys(tenant_name_field, dynamic_data.company_name)

def enter_prefix(driver):
    prefix_field = perform_find_element(driver, "xpath", create_new_tenant_locators.tenant_prefix)
    perform_send_keys(prefix_field, dynamic_data.tenant_prefix)

def enter_company_name(driver):
    company_name_field = perform_find_element(driver, "xpath", create_new_tenant_locators.company_name)
    perform_send_keys(company_name_field, dynamic_data.company_name)

def enter_email(driver):
    email_field = perform_find_element(driver, "xpath", create_new_tenant_locators.email)
    perform_send_keys(email_field, dynamic_data.email) 

def enter_address(driver):
    address_field = perform_find_element(driver, "xpath", create_new_tenant_locators.address)
    perform_send_keys(address_field, dynamic_data.address)

def enter_flat_details(driver):
    appartment_field = perform_find_element(driver, "xpath", create_new_tenant_locators.appartment)
    perform_send_keys(appartment_field, dynamic_data.flat_no)

def enter_country(driver):
    country_drop_down = perform_find_element(driver, "name", create_new_tenant_locators.country_drop_down)
    perform_click(driver, country_drop_down)
    country_field = perform_find_element(driver, "xpath", create_new_tenant_locators.country_option)
    driver.execute_script("arguments[0].scrollIntoView();", country_field)
    driver.execute_script("arguments[0].click();", country_field)

def enter_state(driver):
    state_drop_down = perform_find_element(driver, "name", create_new_tenant_locators.state_drop_down)
    perform_click(driver, state_drop_down)
    state_field = perform_find_element(driver, "xpath", create_new_tenant_locators.state_option)
    driver.execute_script("arguments[0].click();", state_field)

def add_zip_code(driver):
    zipcode_field = perform_find_element(driver, "xpath", create_new_tenant_locators.zip_code)
    perform_send_keys(zipcode_field, dynamic_data.zip_code)

def enter_status(driver):
    status_drop_down = perform_find_element(driver, "name", create_new_tenant_locators.status_drop_down)
    perform_click(driver, status_drop_down)
    status_option = perform_find_element(driver, "xpath", create_new_tenant_locators.status_option)
    driver.execute_script("arguments[0].click();", status_option)

def add_company_profile(driver):
    element = perform_find_element(driver, "xpath", "//label[text()='Company Profile']")
    perform_scroll_to(driver, element)
    profile_field = perform_find_element(driver, "xpath", create_new_tenant_locators.profile_field)
    move_to_element_and_send(driver, profile_field, dynamic_data.profile)
