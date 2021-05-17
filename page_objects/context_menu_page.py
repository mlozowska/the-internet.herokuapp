from tests.helpers.support_functions import *

header = '//*[@id="content"]/ul/li[7]/a'
content = 'content'
box = 'hot-spot'


def click_context_menu_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, header)
    elem = driver_instance.find_element_by_xpath(header)
    elem.click()


def context_menu_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, content)
    return elem.is_displayed()


def right_click_menu(driver_instance):
    right_click_operation(driver_instance, driver_instance.find_element_by_id(box))
