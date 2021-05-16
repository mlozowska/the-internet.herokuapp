import unittest
from selenium import webdriver

from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, drag_drop_page, dropdown_page, status_codes_page, input_page,\
    basic_auth_page, proper_credent_page, forgot_password_page, error_500_page, form_authentication_page, logout_page, hovers_page,\
    not_found_page, context_menu_page, file_upload_page, upload_confirmation_page


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

    # Basic Auth Page Tests
    def test_basic_auth_send_correct_keys(self):
        basic_auth_page.send_correct_keys(self.driver)
        self.assertTrue(proper_credent_page.message_content_visible(self.driver))

    # Forgot Password Page Tests
    def test_forgot_password_content_visible(self):
        forgot_password_page.click_forgot_password_tab(self.driver)
        self.assertTrue(forgot_password_page.forgot_password_content_visible(self.driver))

    def test_enter_email(self):
        forgot_password_page.click_forgot_password_tab(self.driver)
        self.assertTrue(forgot_password_page.send_email(self.driver))

    def test_internal_server_error_visible(self):
        Tests.test_enter_email(self)
        forgot_password_page.click_retrieve_password(self.driver)
        self.assertTrue(error_500_page.internal_server_error(self.driver))

    # Hovers page Tests
    def test_hovers_content_visible(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hovers_content_visible(self.driver))

    def test_hovers_user_one(self):
        Tests.test_hovers_content_visible(self)
        hovers_page.hover_over_element_one_and_click(self.driver)
        self.assertTrue(not_found_page.not_found_message_visible(self.driver))

    def test_hovers_user_two(self):
        Tests.test_hovers_content_visible(self)
        hovers_page.hover_over_element_two_and_click(self.driver)
        self.assertTrue(not_found_page.not_found_message_visible(self.driver))

    def test_hovers_user_three(self):
        Tests.test_hovers_content_visible(self)
        hovers_page.hover_over_element_three_and_click(self.driver)
        self.assertTrue(not_found_page.not_found_message_visible(self.driver))

    # Context Menu Page Test
    def test_context_menu_content_visible(self):
        context_menu_page.click_context_menu_tab(self.driver)
        self.assertTrue(context_menu_page.context_menu_content_visible(self.driver))
        context_menu_page.right_click_menu(self.driver)

    # Upload File Page Tests
    def test_upload_file(self):
        file_upload_page.click_file_upload_tab(self.driver)
        self.assertTrue(file_upload_page.file_upload_content_visible(self.driver))
        file_upload_page.choose_file(self.driver)

    def test_upload_file_confirmation(self):
        Tests.test_upload_file(self)
        upload_confirmation_page.file_uploaded_msg_visible(self.driver)

