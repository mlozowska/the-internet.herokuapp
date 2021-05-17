from tests.helpers.support_functions import *
from time import sleep

form_authentication_header = '//*[@id="content"]/ul/li[21]/a'
form_authentication_content = 'content'
username_field = 'username'
password_field = 'password'
# correct_username = 'tomsmith'
# correct_password = 'SuperSecretPassword!'
# incorrect_username = 'littleprince'
# incorrect_password = 'TopSecret!'
login_button = '//*[@id="login"]/button/i'
invalid_credentials_info = 'flash'


def click_form_authentication_tab(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, form_authentication_header)
    elem = driver_instance.find_element_by_xpath(form_authentication_header)
    elem.click()


def form_authentication_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, form_authentication_content)
    return elem.is_displayed()



def send_correct_data(driver_instance):
    elem1 = driver_instance.find_element_by_id(username_field)
    elem1.send_keys('tomsmith')
    elem2 = driver_instance.find_element_by_xpath(password_field)
    elem2.send_keys('SuperSecretPassword!')
    sleep(3)
    elem3 = driver_instance.find_element_by_xpath(login_button)
    elem3.click()
    sleep(3)


def send_invalid_data(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, username_field)
    elem1 = driver_instance.find_element_by_id(username_field)
    elem1.send_keys('dnanaj')
    elem2 = driver_instance.find_element_by_id(password_field)
    elem2.send_keys('SuperSecret!')
    elem3 = driver_instance.find_element_by_xpath(login_button)
    elem3.click()
    sleep(4)


def invalid_credentials_displayed(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, invalid_credentials_info)
    # elem = driver_instance.find_elememnt_by_id(invalid_credentials_info)
    return elem.is_displayed()

def enter_correct_credentials(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, username_field)
    user_name = driver_instance.find_element_by_id(username_field)
    user_name.send_keys('tomsmith')
    password = driver_instance.find_element_by_id(password_field)
    password.send_keys('SuperSecretPassword!')
    login = driver_instance.find_element_by_xpath(login_button)
    login.click()

    correct_username = 'tomsmith'
    correct_password = 'SuperSecretPassword!'

    if correct_username == user_name.get_attribute(correct_username) or correct_password == password.get_attribute(correct_password):
        return True
    else:
        return False


    # click_login = driver_instance.find_element_by_xpath(login_button)
    # click_login.click()

    # correct_username = 'tomsmith'
    # correct_password = 'SuperSecretPassword!'
    # if correct_username == str(user_name.get_attribute(correct_username)) \
    #         and str(correct_password == password.get_atribute(correct_password)):
    #     return True
    # else:
    #     return False
    # sleep(2)


# def enter_incorrect_credentials(driver_instance):
#     user_name = driver_instance.find_element_by_id(username_field)
#     user_name.send_keys(incorrect_username)
#     password = driver_instance.find_element_by_id(password_field)
#     password.send_keys(incorrect_password)
#     if incorrect_username == user_name.get_attribute(incorrect_username) \
#             and incorrect_password == password.get_atribute(incorrect_password):
#         return False
#     else:
#         return True


# def click_login_button(driver_instance):
#     click_login = driver_instance.find_element_by_xpath(login_button)
#     click_login.click()










