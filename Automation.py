from Drivers.Driver_Factory import initialize_driver
from Pages.login_page import perform_login


driver = initialize_driver()
perform_login(driver)
driver.close