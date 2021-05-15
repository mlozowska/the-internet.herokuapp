from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, element):
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()


def drag_and_drop(driver_instance, elem_1, elem_2):
    action = ActionChains(driver_instance)
    action.drag_and_drop_by_offset(elem_1, 100, 100)
    action.perform()
    action2 = ActionChains(driver_instance)
    action2.drag_and_drop(elem_1, elem_2).perform()


def wait_for_visibility_of_element_xpath(driver_instance, xpath):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_id(driver_instance, id):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_invisibility_of_element_xpath(inv_driver_instance, xpath):
    inv_element = WebDriverWait(inv_driver_instance, 8).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_element
