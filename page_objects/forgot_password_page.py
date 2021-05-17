from tests.helpers.support_functions import *


forgot_password_header = '//*[@id="content"]/ul/li[20]/a'
forgot_password_content = 'content'
email_field = 'email'
retrieve_password_button = '//*[@id="form_submit"]/i'


def click_forgot_password_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, forgot_password_header)
    elem = driver_instance.find_element_by_xpath(forgot_password_header)
    elem.click()


def forgot_password_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, forgot_password_content)
    return elem.is_displayed()


def send_email(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, email_field)
    email_address = driver_instance.find_element_by_id(email_field)
    email_address.send_keys('sxk69578@zwoho.com')

    value = 'sxk69578@zwoho.com'
    if value == email_address.get_attribute("value"):
        return True
    else:
        return False


def click_retrieve_password(driver_instance):
    elem = driver_instance.find_element_by_xpath(retrieve_password_button)
    elem.click()


