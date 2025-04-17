from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        self.find_element(locator).click()
    
    def get_title(self):
        return self.driver.title
    
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    def navigate_to(self, url):
        self.driver.get(url)
    
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown(self, locator, value):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(value)