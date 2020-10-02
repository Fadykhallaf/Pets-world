from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_is_there_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Pepe', self.browser.page_source)

    def tearDown(self) -> None:
        self.browser.quit()
