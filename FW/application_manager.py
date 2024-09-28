from Data.settings import Settings
from FW.FW_Base import FWBase
from FW.driver_instance import DriverInstance
from FW.mail.main_page import MainPage
from FW.mail.search_page import SearchPage


class ApplicationManager:

    def __init__(self):

        self.driver_instance = DriverInstance()
        self.fw_base = FWBase(self)
        self.settings = Settings()
        self.main_page = MainPage(self)
        self.search_page = SearchPage(self)
