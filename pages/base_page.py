# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, value,by=By.XPATH):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def set_text(self, value, text, by=By.XPATH):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def press_enter(self, value,by=By.XPATH):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.send_keys(Keys.ENTER)
