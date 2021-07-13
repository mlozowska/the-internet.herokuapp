import unittest
from selenium import webdriver

from config.test_settings import TestSettings
from page_objects import add_remove_page, drag_drop_page, status_codes_page, context_menu_page, \
    dropdown_page, forgot_password_page, error_500_page, upload_confirmation_page, basic_auth_page, auth_confirm_page, \
    file_upload_page, checkboxes_page, hovers_page, main_page, not_found_page, inputs_page, frames_page, \
    iframe_page, form_authentication_page, logout_page, digest_auth_page, confirm_digest_auth_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Main Page Test
    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    # Add/Remove Element Page Tests
    def test_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test_remove_element(self):
        Tests.test_add_element(self)
        add_remove_page.remove_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    # Basic Auth Page Test
    def test_basic_auth_send_correct_keys(self):
        basic_auth_page.send_correct_keys(self.driver)
        self.assertTrue(auth_confirm_page.message_content_visible(self.driver))

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

    # Checkboxes Page Test
    def test_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_content_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    # Drag and Drop Page Tests
    def test_drag_drop_content(self):
        drag_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_and_drop_content_visible(self.driver))

    def test_drag_and_drop_columns(self):
        drag_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_and_drop_element(self.driver))

    # Drop-down Page Tests
    def test_dropdown_option_one(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test_dropdown_option_two(self):
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
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test_correct_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test_incorrect_input(self):
        inputs_page.click_input_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

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

    # Context Menu Page Test
    def test_context_menu_content_visible(self):
        context_menu_page.click_context_menu_tab(self.driver)
        self.assertTrue(context_menu_page.context_menu_content_visible(self.driver))
        context_menu_page.right_click_menu(self.driver)

    # Digest Authentication Page Test
    def test_digest_auth_send_correct_keys(self):
        digest_auth_page.send_correct_keys(self.driver)
        self.assertTrue(confirm_digest_auth_page.confirmation_message_visible(self.driver))

    # Upload File Page Tests
    def test_upload_file(self):
        file_upload_page.click_file_upload_tab(self.driver)
        self.assertTrue(file_upload_page.file_upload_content_visible(self.driver))
        file_upload_page.choose_file(self.driver)

    def test_upload_file_confirmation(self):
        Tests.test_upload_file(self)
        upload_confirmation_page.file_uploaded_msg_visible(self.driver)

    # Frames Pages Tests
    def test_frames_content_visible(self):
        frames_page.click_frames_header(self.driver)
        self.assertTrue(frames_page.frames_content_visible(self.driver))

    def test_iframe_content_visible(self):
        Tests.test_frames_content_visible(self)
        frames_page.click_iframe_header(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    # Form Authentication Page Tests
    def test_send_correct_credentials(self):
        form_authentication_page.click_form_authentication_tab(self.driver)
        form_authentication_page.send_valid_data(self.driver)
        self.assertTrue(logout_page.secure_area_message_visible(self.driver))

    def test_send_incorrect_credentials(self):
        form_authentication_page.click_form_authentication_tab(self.driver)
        self.assertTrue(form_authentication_page.send_invalid_data(self.driver))




if __name__ == '__main__':
    unittest.main()