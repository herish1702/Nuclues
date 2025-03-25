from selenium import webdriver

from Data.Static_Data import static_data


def initialize_drivers():
    browsers_list = ["chrome", "firefox", "edge", "safari"]
    drivers = {}

    for browser in browsers_list:
        try:
            if browser == "chrome":
                drivers[browser] = webdriver.Chrome()

            elif browser == "firefox":
                drivers[browser] = webdriver.Firefox()

            elif browser == "edge":
                drivers[browser] = webdriver.Edge()

            elif browser == "safari":
                drivers[browser] = webdriver.Safari()

            drivers[browser].maximize_window()
            drivers[browser].get(static_data.url)

        except Exception as e:
            print(f"Failed to initialize {browser}: {e}")
            continue

    return drivers