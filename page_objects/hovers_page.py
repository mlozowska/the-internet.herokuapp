from tests.helpers.support_functions import *

hovers_header = '//*[@id="content"]/ul/li[25]/a'
hovers_content = 'content'
user_one = '//*[@id="content"]/div/div[1]/img'
user_two = '//*[@id="content"]/div/div[2]/img'
user_three = '//*[@id="content"]/div/div[3]/img'
link_one = '//*[@id="content"]/div/div[1]/div/a'
link_two = '//*[@id="content"]/div/div[2]/div/a'
link_three = '//*[@id="content"]/div/div[3]/div/a'


def click_hovers_tab(driver_instance):
    elem = driver_instance.find_element_by_xpath(hovers_header)
    elem.click()


def hovers_content_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, hovers_content)
    elem = driver_instance.find_element_by_id(hovers_content)
    return elem.is_displayed()


def hover_over_element_one_and_click(driver_instance):
    hover_over_element(driver_instance, driver_instance.find_element_by_xpath(user_one))
    elem = driver_instance.find_element_by_xpath(link_one)
    elem.click()


def hover_over_element_two_and_click(driver_instance):
    hover_over_element(driver_instance, driver_instance.find_element_by_xpath(user_two))
    elem = driver_instance.find_element_by_xpath(link_two)
    elem.click()


def hover_over_element_three_and_click(driver_instance):
    hover_over_element(driver_instance, driver_instance.find_element_by_xpath(user_three))
    elem = driver_instance.find_element_by_xpath(link_three)
    elem.click()
