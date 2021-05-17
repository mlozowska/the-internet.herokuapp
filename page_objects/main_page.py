from tests.helpers.support_functions import *

main_page_header = 'heading'
main_page_content = 'content'


def content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, main_page_content)
    return elem.is_displayed()
