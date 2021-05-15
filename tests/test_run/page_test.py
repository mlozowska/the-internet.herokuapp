import unittest
from selenium import webdriver

from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, drag_drop_page, dropdown_page, status_codes_page, input_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Main age Test
    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    # Checkboxes Page Test
    def test_checkboxes(self):
        # klikam w tab
        checkboxes_page.click_checkboxes_tab(self.driver)
        # asercja ze contenct ok
        self.assertTrue(checkboxes_page.checkboxes_content_visible(self.driver))
        # test - klikam checkboxes
        checkboxes_page.click_checkboxes(self.driver)

    # Drag and Drop Page Tests
    def test_drag_drop_content(self):
        drag_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_and_drop_content_visible(self.driver))

    def test_drag_and_drop_columns(self):
        drag_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_and_drop_element(self.driver))

    # Drop-down Page Tests
    def test_dropdown_first_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test_dropdown_second_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_second_dropdown_value(self.driver)

    # Status Codes Page Tests
    def test_status_code_visible(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))

    def test_status_code_200(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_code_200(self.driver))

    def test_status_code_301(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_code_301(self.driver))

    def test_status_code_404(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_code_404(self.driver))

    def test_status_code_500(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_code_500(self.driver))

    # Input Page Tests
    def test_input_content_visible(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.input_content_visible(self.driver))

    def test_correct_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test_incorrect_input(self):
        input_page.click_input_tab(self.driver)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))