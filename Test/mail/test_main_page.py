import time

from Test.test_base import TestBase


class TestMainPage(TestBase):

    def test_search(self):
        search_page = self.APP.main_page.search('НГИЭУ')
        assert search_page.check_site_in_page('Княгининский университет')
