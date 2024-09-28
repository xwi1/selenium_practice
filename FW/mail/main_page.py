from selenium.webdriver.common.by import By

from FW.mail.any_page import AnyPage


class Locator:
    button_search = (By.XPATH, '//button[@data-testid="search-button"]')
    iframe_search = (By.XPATH, '//iframe[contains(@class, "search-arrow")]')
    input_search = (By.XPATH, '//input[@name="text"]')


class MainPage(AnyPage):

    def search(self, text):
        self.send_keys_in_iframe(Locator.iframe_search, text, locator_el=Locator.input_search)
        self.click_element(Locator.button_search)
        return self.manager.search_page

