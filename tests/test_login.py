# tests/test_login.py
import os
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from configparser import ConfigParser
import sys
print(sys.path)
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        project_directory = os.path.dirname(os.path.abspath(__file__))

        self.config=ConfigParser()
        config_dir=os.path.join(project_directory, "..", "config.ini")
        self.config.read(config_dir)

        drivers_directory = os.path.join(project_directory, "..", "drivers")
        chrome_driver_path = os.path.join(drivers_directory, "chromedriver.exe")
        edge_driver_path = os.path.join(drivers_directory, "msedgedriver.exe")

        service = Service(chrome_driver_path)
        edge_service = Service(edge_driver_path)

        self.driver = webdriver.Chrome(service=service)
        logging.info("Test setup completed.")

        login_page_url = self.config.get("Urls", "login_page")
        self.driver.get(login_page_url)
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        username=self.config.get("Credentials","username")
        password = self.config.get("Credentials", "password")

        self.login_page.enter_username(username)
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()
        logging.info("Successful logging completed")

        # Add assertions or further test steps as needed

    def tearDown(self):
        logging.info("Tearing down the test")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
