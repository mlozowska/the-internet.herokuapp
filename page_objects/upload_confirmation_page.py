from tests.helpers.support_functions import *


message = '//*[@id="content"]/div/h3'


def file_uploaded_msg_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, message)
    elem = driver_instance.find_element_by_xpath(message)
    return elem.is_displayed()