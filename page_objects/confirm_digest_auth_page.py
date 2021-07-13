from helpers.support_functions import *


congrats_message = '//*[@id="content"]/div/p'


def confirmation_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance. congrats_message)
    confirmation_msg = driver_instance.find_element_by_xpath(congrats_message)
    value = "Congratulations! You must have the proper credentials."
    if value == confirmation_msg.get_attribute("value"):
        return True
    else:
        return False


# def send_email(driver_instance):
#     wait_for_visibility_of_element_id(driver_instance, email_field)
#     email_address = driver_instance.find_element_by_id(email_field)
#     email_address.send_keys('sxk69578@zwoho.com')
#     value = 'sxk69578@zwoho.com'
#     if value == email_address.get_attribute("value"):
#         return True
#     else:
#         return False