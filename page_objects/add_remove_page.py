from tests.helpers.support_functions import *

header = '//*[@id="content"]/ul/li[2]/a'
content = 'content'
add_element_button = '//*[@id="content"]/div/button'
remove_element_button = '//*[@id="elements"]/button'


def click_add_remove_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, header)
    elem = driver_instance.find_element_by_xpath(header)
    elem.click()


def add_remove_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, content)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(add_element_button)
    elem.click()


def remove_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(remove_element_button)
    elem.click()
    wait_for_invisibility_of_element_xpath(remove_element_button)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_xpath(driver_instance, remove_element_button)
        return True
    except NoSuchElementException:
        return False