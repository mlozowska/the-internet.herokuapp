from tests.helpers.support_functions import *

basic_auth_tab = '//*[@id="content"]/ul/li[3]/a'


def click_basic_auth_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, basic_auth_tab)
    elem = driver_instance.find_element_by_xpath(basic_auth_tab)
    elem.click()


def send_correct_keys(driver_instance):
    # add username and password credentials to the link: http://username:password@rest of the link
    driver_instance.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

