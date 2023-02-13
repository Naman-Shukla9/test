import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
@pytest.fixture()
def initiate_driver():

    driver.get("https://www.boat-lifestyle.com")
    time.sleep(5)
    driver.maximize_window()
    yield driver

    driver.quit()