from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Data.Static_Data import static_data


def initialize_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver.get(static_data.url)
    driver.get(static_data.url)
    return driver

def initialize_firefox_driver():
    firefox_options = FirefoxOptions()
    # firefox_options.add_argument("--headless")  # Uncomment for headless mode
    firefox_options.set_preference("detach", True) 
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver
    

def initialize_edge_driver():
    edge_options = EdgeOptions()
    # edge_options.add_argument("--headless")  # Uncomment for headless mode
    edge_options.add_experimental_option("detach", True)  
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get(static_data.url)
    return driver


def initialize_safari_driver():
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get(static_data.url)
    return driver


