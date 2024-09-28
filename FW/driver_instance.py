from selenium import webdriver

from Data.settings import Settings


class DriverInstance:

    def __init__(self):
        self.settings = Settings

    driver = None

    def get_driver(self):
        option = webdriver.ChromeOptions()

        if self.settings.browser['NoSandBox']:
            option.add_argument('--no-sandbox')

        if self.settings.browser['Headless']:
            option.add_argument('--headless')
            option.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=option)
        if self.settings.browser['Headless'] is False:
            self.driver.maximize_window()

        return self.driver
    
    def stop_driver(self):
        try:
            self.driver.quit()
            self.driver = None
        except:
            self.driver = None


