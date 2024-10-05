from selenium.webdriver.common.by import By
import time

from FW.mail.any_page import AnyPage


class Locator:
    iframe_search = (By.XPATH, '//iframe[@class="yandex-frame"]')
    wiki_link = (By.XPATH, '//a[contains(@href, "wiki")]')
    knyag_text = (By.XPATH, '//*[contains(text(), "Княгинино")]')


class SearchPage(AnyPage):

    def check_site_in_page(self, site_name):
        return self.check_element_in_page((By.XPATH, f'//span[@role="text" and text()="{site_name}"]'), frame_locator=Locator.iframe_search)
    
    def open_wiki_page(self):
        self.click_element(locator=Locator.wiki_link)
        time.sleep(10)
        elements = self.find_elements(Locator.knyag_text)
        assert len(elements) > 0, "Элементов с надписью 'Княгинино' не найдено"



        
    