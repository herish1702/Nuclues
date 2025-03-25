from Drivers.Driver_Factory import initialize_driver
from Pages.login_page import perform_login
from Pages.tenant_page import add_new_tenant

driver = initialize_driver()
perform_login(driver)
add_new_tenant(driver)

