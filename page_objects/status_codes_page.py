from tests.helpers.support_functions import *
from requests import api

status_codes_header = '//*[@id="content"]/ul/li[42]/a'
status_codes_content = 'content'
code_200 = '//*[@id="content"]/div/ul/li[1]/a'
code_301 = '//*[@id="content"]/div/ul/li[2]/a'
code_404 = '//*[@id="content"]/div/ul/li[3]/a'
code_500 = '//*[@id="content"]/div/ul/li[4]/a'


def click_status_codes_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, status_codes_header)
    elem = driver_instance.find_element_by_xpath(status_codes_header)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_codes_content)
    return elem.is_displayed()


def status_code_200(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_200)
    status_200 = driver_instance.find_element_by_xpath(code_200)
    link_200 = status_200.get_attribute('href')
    r = api.get(link_200)
    if r.status_code == 200:
        return True
    else:
        return False


def status_code_301(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_301)
    status_301 = driver_instance.find_element_by_xpath(code_301)
    link_301 = status_301.get_attribute('href')
    r = api.get(link_301)
    if r.status_code == 301:
        return True
    else:
        return False


def status_code_404(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_404)
    status_404 = driver_instance.find_element_by_xpath(code_404)
    link_404 = status_404.get_attribute('href')
    r = api.get(link_404)
    if r.status_code == 404:
        return True
    else:
        return False


def status_code_500(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_500)
    status_500 = driver_instance.find_element_by_xpath(code_500)
    link_500 = status_500.get_attribute('href')
    r = api.get(link_500)
    if r.status_code == 500:
        return True
    else:
        return False