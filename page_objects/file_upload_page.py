from tests.helpers.support_functions import *

header = '//*[@id="content"]/ul/li[18]/a'
content = 'content'
choose_file_button = 'file-upload'
upload_button = 'file-submit'


def click_file_upload_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, header)
    elem = driver_instance.find_element_by_xpath(header)
    elem.click()


def file_upload_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, content)
    return elem.is_displayed()


def choose_file(driver_instance):
    elem_1 = driver_instance.find_element_by_id(choose_file_button)
    # use double backslashes
    elem_1.send_keys("C:\\Users\\Administrator\\Desktop\\attachment1.pdf")
    elem_2 = driver_instance.find_element_by_id(upload_button)
    elem_2.click()
