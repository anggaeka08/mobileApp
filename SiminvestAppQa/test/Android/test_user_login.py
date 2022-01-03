import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time

LoginPage = LoginPage()
HomePage = HomePage()

#Test cases for login with valid new number
@pytest.mark.SMMA_001
@pytest.mark.Android
def test_login_with_valid_mobile_no():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(generate_random_integer(length=7, prefix='844'))
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.set_pin(user_data['setup_pin_value'])
    LoginPage.verify_risk_profile_page()
    LoginPage.click_agresif_profile()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page()

#Test case for login with reg Number
@pytest.mark.SMMA_002
@pytest.mark.Android
def test_login_with_invalid_no_less_then_10():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['wrong_length_no'])
    LoginPage.verify_selanjutnya()

#Test case for
@pytest.mark.SMMA_003
@pytest.mark.Android
def test_login_with_valid_reg_mobile_no():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page_reg_user()

#Test case for received again otp
@pytest.mark.SMMA_009
@pytest.mark.Android
def test_did_not_receive_the_otp():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    time.sleep(35)
    LoginPage.click_Kirim_Ulang()

#Test case for re-enter phone no by back after otp page
@pytest.mark.SMMA_010
@pytest.mark.Android
def test_re_enter_phone_no_after_otp():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(user_data['reg_no'])
    LoginPage.click_back_button_otp_page()
    LoginPage.type_mobile_no(user_data['unkyc_reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(user_data['unkyc_reg_no'])

#Test case for check_login_with_reset_code_functionality after pin error
@pytest.mark.SMMA_013
@pytest.mark.Android
def test_check_login_with_reset_code_functionality_after_pin_error():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_wrong_pin()
    LoginPage.verify_wrong_pin_message()
    LoginPage.click_on_reset_pin()
    LoginPage.enter_otp(user_data['valid_otp'])
    time.sleep(2)
    LoginPage.set_pin(user_data['setup_pin_value'])
    time.sleep(3)
    LoginPage.set_pin(user_data['setup_pin_value'])
    time.sleep(2)
    LoginPage.confirm_pin_reset()
    time.sleep(10)
    LoginPage.verify_redicrect_to_pin_page()

#Test case for check security flow
@pytest.mark.SMMA_018
@pytest.mark.Android
def test_check_valid_input_security_code_flow():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page_reg_user()

#Test cases for check reset pin without failed login
@pytest.mark.SMMA_019
@pytest.mark.Android
def test_check_reset_pin_funtionality_without_failed_login():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.click_on_reset_pin()
    LoginPage.enter_otp(user_data['valid_otp'])
    time.sleep(2)
    LoginPage.set_pin(user_data['setup_pin_value'])
    time.sleep(3)
    LoginPage.set_pin(user_data['setup_pin_value'])
    time.sleep(2)
    LoginPage.confirm_pin_reset()
    time.sleep(10)
    LoginPage.verify_redicrect_to_pin_page()

#Test cases for check invalid input security code flow
@pytest.mark.SMMA_020
@pytest.mark.Android
def test_check_invalid_input_security_code_flow():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_wrong_pin()
    time.sleep(2)
    LoginPage.verify_wrong_pin_message()


#Test case for  Check the security code screen after session timeout
@pytest.mark.SMMA_021
@pytest.mark.Android
def test_security_code_check_after_timeout_session():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page_reg_user()
    LoginPage.app_in_background(300)
    time.sleep(2)
    LoginPage.enter_pin()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page_reg_user()

#Test Case for logout user from security page
@pytest.mark.SMMA_022
@pytest.mark.Android
def test_logout_feature_from_security_code_page():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.click_on_enterPin_logout_button()
    LoginPage.verify_starting_page()

#Test case for fingerprint enable and disable
@pytest.mark.SMMA_015
@pytest.mark.Android
def test_enable_and_disable_finger_print():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(generate_random_integer(length=7, prefix='844'))
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.set_pin(user_data['setup_pin_value'])
    LoginPage.verify_risk_profile_page()
    LoginPage.click_agresif_profile()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page()
    LoginPage.click_on_profile_btn()
    LoginPage.enable_finger_print()
    time.sleep(3)
    LoginPage.disable_finger_print()

