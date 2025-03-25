from Drivers.Driver_Factories import initialize_drivers
from Pages.forgot_password_page import test_forgot_password
from Pages.login_page import perform_login
from Utils.Utils import get_current_url, take_full_screenshot



drivers = initialize_drivers()

for browser_name, driver in drivers.items():
    print(f"Running tests on {browser_name}:")

    try:
        test_forgot_password(driver)
        perform_login(driver) 
        print()

    except Exception as e:
        print(f"Error in {browser_name}: {e}")
        take_full_screenshot(driver)
        get_current_url(driver)

    finally:
        driver.close()