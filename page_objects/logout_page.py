from tests.helpers.support_functions import *

data_alert = 'flash'
logout_button = '//*[@id="content"]/div/a/i'


def secure_area_message_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, data_alert)
    elem = driver_instance.find_element_by_id(data_alert)
    return elem.is_displayed()


def logged_out(driver_instance):
    elem = driver_instance.find_element_by_id(logout_button)
    elem.click()
