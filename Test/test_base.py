from FW.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        pass

    def setup_method(self):
        self.APP.fw_base.go_to_page(self.APP.settings.page['Link'])

    def teardown_class(self):
        pass

    def teardown_method(self):
        pass