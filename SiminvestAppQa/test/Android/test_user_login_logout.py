import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time

LoginPage = LoginPage()
HomePage = HomePage()

# Verify that user should be redirecting to the welcome page after open the application.
@pytest.mark.SMMA_001
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_welcome_after_open_app():
    LoginPage.verify_starting_page()

# Verify that user should be redirecting to the input phone number page when user tap on 'Mulai Sekarang' button
@pytest.mark.SMMA_002
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_phone_no_page_after_click_MulaiSekarang():
    LoginPage.launch_app_again()
    LoginPage.verify_starting_page()
    LoginPage.click_mulai_sekarang()
    LoginPage.verify_mobile_no_page()

# Verify that 'Selanjutnya' button should be displayed activate after entering 7 digit phone number.
@pytest.mark.SMMA_004
@pytest.mark.Android
@pytest.mark.login
def test_verify_Selanjutnya_button_activate_after_6_digit_no():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['wrong_length_no'])
    LoginPage.verify_selanjutnya()

# Verify that user should redirect to the security code page after tap on 'Selanjutnya' button when user is on enter mobile number page
@pytest.mark.SMMA_005
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_security_code_page_by_using_valid_no():
    number = generate_random_integer(length=7, prefix='844')
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(number)
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(number)

# Verify that user should redirect to the set up pin number page after entering the 4 digit security code when user login account first time
@pytest.mark.SMMA_006
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_setup_pin_by_using_valid_no():
    number = generate_random_integer(length=7, prefix='844')
    #LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(number)
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(number)
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.verify_setup_pin_page()

# Verify that user should redirect to the home page after entering the 6 digit pin number
@pytest.mark.SMMA_007
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_home_page_after_enter_pin():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    #LoginPage.close_home_page_banner()
    LoginPage.verify_home_page_reg_user()

# Verify that user should be redirecting to the welcome page after tap on logout link under profile section
@pytest.mark.SMMA_008
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_welcome_page_after_logout_click():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.click_on_enterPin_logout_button()
    LoginPage.verify_starting_page()

#Validate the first time login user should be redirected to type of risk profile selection page when user enter 6 digit pin
@pytest.mark.SMMA_010
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_risk_profile_page_after_enter_pin_for_new_no():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(generate_random_integer(length=7, prefix='844'))
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.set_pin(user_data['setup_pin_value'])
    LoginPage.verify_risk_profile_page()

# Validate user should redirected to home page when user login with same account 2nd time and in future.
@pytest.mark.SMMA_011
@pytest.mark.Android
@pytest.mark.login
def test_verify_redirect_to_home_when_login_with_same_no_second_time():
    number = generate_random_integer(length=7, prefix='844')
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(number)
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.set_pin(user_data['setup_pin_value'])
    LoginPage.verify_risk_profile_page()
    LoginPage.click_agresif_profile()
    LoginPage.verify_home_page()
    #launch again and use same no
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(number)
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    LoginPage.verify_home_page()

# Validate login in with invalid mobile number
@pytest.mark.SMMA_012
@pytest.mark.Android
@pytest.mark.login
def test_validate_login_with_invalid_mobile_number():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['wrong_length_no'])
    LoginPage.verify_selanjutnya()

# Validate enter mobile number page should accept maximum 12 digit number
@pytest.mark.SMMA_013
@pytest.mark.Android
@pytest.mark.login
def test_validate_entry_of_max_12_digit_no_in_phone_section():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['max_lenth_no'])
    LoginPage.verify_count_of_mobile_no(user_data['max_lenth_no'])

# Validate login with invalid PIN
@pytest.mark.SMMA_015
@pytest.mark.Android
@pytest.mark.login
def test_validate_login_with_invalid_phone():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_wrong_pin()
    LoginPage.verify_wrong_pin_message()

# Validate reset pin functionality is working fine
@pytest.mark.SMMA_016
@pytest.mark.Android
@pytest.mark.login
def test_validate_reset_pin_functinality():
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
    LoginPage.verify_redirect_to_pin_page()
    LoginPage.enter_pin()
    LoginPage.verify_home_page_reg_user()

# Validate user is able to logout from the enter pin page.
@pytest.mark.SMMA_017
@pytest.mark.Android
@pytest.mark.login
def test_validate_user_able_to_logout_from_enter_pin_page():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.click_on_enterPin_logout_button()
    LoginPage.verify_starting_page()

# validate the back button is working fine at enter OTP page
@pytest.mark.SMMA_018
@pytest.mark.Android
@pytest.mark.login
def test_validate_back_btn_at_enter_otp_page():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(user_data['reg_no'])
    LoginPage.click_back_button_otp_page()
    LoginPage.verify_mobile_no_page()

# Validate user is able to login after user click on resend OTP page
@pytest.mark.SMMA_021
@pytest.mark.Android
@pytest.mark.login
def test_validate_login_after_resend_otp():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    time.sleep(35)
    LoginPage.click_Kirim_Ulang()
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.enter_pin()
    LoginPage.verify_home_page_reg_user()

# validate the timeout of OTP page is running even after user switch the application while timeout is running.
@pytest.mark.SMMA_022
@pytest.mark.Android
@pytest.mark.login
def test_validate_otp_timout_timmer_while_app_in_backgroud():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['reg_no'])
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_timmer()

# Validate reset functionality is working fine on login page.
@pytest.mark.SMMA_023
@pytest.mark.Android
@pytest.mark.login
def test_validate_reset_functionality_working_fine_on_login_page():
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
    LoginPage.verify_redirect_to_pin_page()
    LoginPage.enter_pin()
    LoginPage.verify_home_page_reg_user()