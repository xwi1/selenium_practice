from selenium.webdriver.common.by import By

from FW.mail.any_page import AnyPage


class Locator:
    iframe_search = (By.XPATH, '//iframe[@class="yandex-frame"]')


class SearchPage(AnyPage):

    def check_site_in_page(self, site_name):
        return self.check_element_in_page((By.XPATH, f'//span[@role="text" and text()="{site_name}"]'), frame_locator=Locator.iframe_search)
