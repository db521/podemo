from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
class Display_wait():
    def __init__(self,driver):
        self.driver = driver

    def visit_url(self,url):
        try:
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get(url)

        except Exception as e:
            raise e

    def get_element_display_wait(self,Location_mode,location_expression):
        try:

            Page_element = WebDriverWait(self.driver,30).until(lambda x:self.driver.find_element(by=Location_mode,value=location_expression))
            return Page_element
        except Exception as e:
            raise e