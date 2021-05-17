from tests.helpers.support_functions import *

drag_drop_header = '//*[@id="content"]/ul/li[10]/a'
drag_drop_content = 'content'
column_a = 'column-a'
column_b = 'column-b'


def click_drag_and_drop_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, drag_drop_header)
    elem = driver_instance.find_element_by_xpath(drag_drop_header)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, drag_drop_content)
    return elem.is_displayed()


def drag_and_drop_element(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, drag_drop_content)
    elem_1 = driver_instance.find_element_by_id(column_a)
    elem_2 = driver_instance.find_element_by_id(column_b)
    drag_and_drop(driver_instance, elem_1, elem_2)
    return True

