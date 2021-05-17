from tests.helpers.support_functions import *

message = '/html/body/h1'


def internal_server_error(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, message)
    elem = driver_instance.find_element_by_xpath(message)
    return elem.is_displayed()