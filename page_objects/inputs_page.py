from helpers.support_functions import *

input_header = '//*[@id="content"]/ul/li[27]/a'
input_content = 'content'
input_field = '//*[@id="content"]/div/div/div/input'


def click_input_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, input_header)
    elem = driver_instance.find_element_by_xpath(input_header)
    elem.click()


def input_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, input_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, input_field)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('123321')
    value = 123321
    if value == int(elem.get_attribute("value")):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, input_field)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True

