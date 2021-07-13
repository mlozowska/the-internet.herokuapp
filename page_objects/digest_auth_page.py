from helpers.support_functions import *


header = '//*[@id="content"]/ul/li[8]/a'


def click_context_menu_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, header)
    elem = driver_instance.find_element_by_xpath(header)
    elem.click()


def send_correct_keys(driver_instance):
    # add the username and password credentials to the link: http://username:password@rest of the link
    driver_instance.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")