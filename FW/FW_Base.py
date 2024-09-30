from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FWBase:

    def __init__(self, application_manager):
        self.manager = application_manager

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def click_element(self, locator):
        el = self.find_element(locator)
        driver = self.GetDriver()
        driver.execute_script("arguments[0].click();", el)
        return self
    
    def switch_to_next_tab(self):
        driver = self.GetDriver()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])

        # Ожидание для того, чтобы можно было страницу посмотреть :)


    def find_elements(self, locator, wait=30):
        return WebDriverWait(self.GetDriver(), wait).until(EC.presence_of_all_elements_located(locator))

    def find_element(self, locator, wait=30):
        return WebDriverWait(self.GetDriver(), wait).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)
        return self

    def clear_keys(self, locator):
        self.find_element(locator).send_keys(Keys.LEFT_CONTROL + 'a' + Keys.DELETE)
        return self

    def send_keys_in_iframe(self, locator_frame, text, locator_el=None):
        frame = self.find_element(locator_frame)
        self.GetDriver().switch_to.frame(frame)
        if locator_el is None:
            locator_el = (By.XPATH, 'html/body')
        self.send_keys(locator_el, text)
        self.GetDriver().switch_to.default_content()
        return self

    def go_to_page(self, page):
        self.GetDriver().get(page)
        return self

    def check_element_in_page(self, locator, frame_locator=None):
        try:
            if frame_locator is not None:
                frame_el = self.find_element(frame_locator)
                self.GetDriver().switch_to.frame(frame_el)
                self.find_element(locator, wait=3)
                self.GetDriver().switch_to.default_content()
                return True
            self.find_element(locator, wait=3)
            return True
        except:
            return False

    def scroll_to_element(self, locator, offset_x=0, offset_y=0):
        web_element = self.find_element(locator)
        element = web_element.location_once_scrolled_into_view
        script = "window.scrollBy(" + str(element['x'] + offset_x) + ", " + str(element['y'] + offset_y) + ")"
        self.GetDriver().execute_script(script)
        return web_element

    def refresh_page(self):
        self.GetDriver().refresh()
        return self
