import time

from Test.test_base import TestBase


class TestMainPage(TestBase):

    def test_search(self):
        search_page = self.APP.main_page.search('Княгинино')
        search_page.open_wiki_page()

