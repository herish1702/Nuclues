from Actions.Perform_Driver_Action import perform_click, perform_find_element
from Locators.navbar_locators import navbar_locator


def click_dashobard(driver):
    dashboard_option = perform_find_element(driver, "xpath", navbar_locator.dashboard)
    perform_click(driver, dashboard_option)

def click_tenant(driver):
    tenant_option = perform_find_element(driver, "xpath", navbar_locator.tenant)
    perform_click(driver, tenant_option)

def click_module(driver):
    module_option = perform_find_element(driver, "xpath", navbar_locator.module)
    perform_click(driver, module_option)
