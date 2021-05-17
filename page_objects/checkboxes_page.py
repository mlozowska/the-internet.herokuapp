from tests.helpers.support_functions import *

checkboxes_tab = '//*[@id="content"]/ul/li[6]/a'
all_checkboxes = 'checkboxes'
checkbox_1 = '//*[@id="checkboxes"]/input[1]'
checkbox_2 = '//*[@id="checkboxes"]/input[2]'


def click_checkboxes_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, checkboxes_tab)
    elem = driver_instance.find_element_by_xpath(checkboxes_tab)
    elem.click()


def checkboxes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, all_checkboxes)
    return elem.is_displayed()


def click_checkboxes(driver_instance):
    elem_1 = driver_instance.find_element_by_xpath(checkbox_1)
    elem_1.click()
    elem_2 = driver_instance.find_element_by_xpath(checkbox_2)
    elem_2.click()



