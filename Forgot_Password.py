from Drivers.Driver_Factory import initialize_driver, initialize_edge_driver, initialize_firefox_driver, initialize_safari_driver
from Pages.forgot_password_page import test_forgot_password
from Pages.login_page import perform_login

driver = initialize_safari_driver()

test_forgot_password(driver)
perform_login(driver) 