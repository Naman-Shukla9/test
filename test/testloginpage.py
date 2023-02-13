import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.loginpageutilities import LoginPageFunctions

from page.homepagelocators import *

class TestHome_page():
    @pytest.mark.usefixtures("initiate_driver")


    def test_click_on_login_wrong_password(self, initiate_driver):
        driver = initiate_driver
        driver.find_element(by=By.CSS_SELECTOR, value=login_icon).click()
        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value=loginbuttonclick).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, email).send_keys("shuklanaman262@gmail.com")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, password).send_keys("boat@12345")
        time.sleep(2)
        driver.find_element(By.XPATH, login_click).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, error_msg))
        )
        email_error_msg = driver.find_element(by=By.XPATH, value=error_msg)
        assert email_error_msg.text == "Incorrect email or password.", "password incorrect message is not displayed"


    def test_click_on_login_wrong_email(self, initiate_driver):
        driver = initiate_driver
        driver.find_element(by=By.CSS_SELECTOR, value=login_icon).click()
        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value=loginbuttonclick).click()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, email).send_keys("shuklanaman862@gmail.com")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, password).send_keys("boat@123")
        time.sleep(2)
        driver.find_element(By.XPATH, login_click).click()
        time.sleep(5)
        email_error_msg = driver.find_element(by=By.XPATH,value=error_msg)
        assert email_error_msg.text == "Incorrect email or password.", "Email incorrect message is not displayed"



    def test_click_on_login_wrong_email_or_password(self, initiate_driver):
        driver = initiate_driver
        driver.find_element(by=By.CSS_SELECTOR, value=login_icon).click()
        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value=loginbuttonclick).click()
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, email).send_keys("shuklanaman862@gmail.com")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, password).send_keys("boat@1234")
        time.sleep(2)
        driver.find_element(By.XPATH, login_click).click()
        time.sleep(5)
        email_error_msg = driver.find_element(by=By.XPATH, value=error_msg)
        assert email_error_msg.text == "Incorrect email or password.", "Email or password incorrect message is not displayed"

    def test_offer(self, initiate_driver):
        self.test_click_on_login(initiate_driver)

        driver = initiate_driver
        driver.find_element(by=By.XPATH,value=offer).click()

    def test_search_box(self, initiate_driver):
        driver = initiate_driver
        driver.find_element(By.CSS_SELECTOR,search_box).send_keys("boat basshead 242")
        time.sleep(4)

    def test_bond_with_boat(self, initiate_driver):
        self.test_click_on_login(initiate_driver)

        driver = initiate_driver
        driver.find_element(by=By.CSS_SELECTOR, value=bond_with_boat).click()
        time.sleep(4)

    def test_click_on_login(self,initiate_driver):
        driver= initiate_driver
        LoginPageFunctions().click_on(login_icon)
        time.sleep(3)
        driver.find_element(by=By.CSS_SELECTOR, value=loginbuttonclick).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, email).send_keys("shuklanaman262@gmail.com")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, password).send_keys("boat@123")
        time.sleep(2)
        driver.find_element(By.XPATH, login_click).click()
        time.sleep(5)