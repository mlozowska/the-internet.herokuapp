from tests.helpers.support_functions import *


basic_auth_message = '//*[@id="content"]/div/p'


def message_content_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, basic_auth_message)
    elem = driver_instance.find_element_by_xpath(basic_auth_message)
    return elem.is_displayed()
