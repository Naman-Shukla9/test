import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from Config.configdata import explicit_wait_time
from page.loginpagelocators import *
from conftest import *

class LoginPageFunctions:
    def click_on(self,element):
        if element.startswith('//'):
            driver.find_element(by=By.XPATH, value=element).click()
        else:
            driver.find_element(by=By.CSS_SELECTOR, value=element).click()
