from tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select

dropdown_header = '//*[@id="content"]/ul/li[11]/a'
dropdown_content = 'content'
dropdown_field = 'dropdown'


def click_dropdown_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, dropdown_header)
    elem = driver_instance.find_element_by_xpath(dropdown_header)
    elem.click()


def dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, dropdown_content)
    return elem.is_displayed()


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdown_field))
    wait_for_visibility_of_element_id(driver_instance, dropdown_field)
    elem_list.select_by_index(1)


def get_second_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdown_field))
    wait_for_visibility_of_element_id(driver_instance, dropdown_field)
    elem_list.select_by_index(2)


