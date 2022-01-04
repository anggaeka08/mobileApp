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
def test_verify_redirect_to_welcome_after_open_app():
    LoginPage.verify_starting_page()

# Verify that user should be redirecting to the input phone number page when user tap on 'Mulai Sekarang' button
@pytest.mark.SMMA_002
@pytest.mark.Android
def test_verify_redirect_to_phone_no_page_after_click_MulaiSekarang():
    LoginPage.launch_app_again()
    LoginPage.verify_starting_page()
    LoginPage.click_mulai_sekarang()
    LoginPage.verify_mobile_no_page()

# Verify that 'Selanjutnya' button should be displayed activate after entering 7 digit phone number.
@pytest.mark.SMMA_004
@pytest.mark.Android
def test_verify_Selanjutnya_button_activate_after_6_digit_no():
    LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(user_data['wrong_length_no'])
    LoginPage.verify_selanjutnya()

# Verify that user should redirect to the security code page after tap on 'Selanjutnya' button when user is on enter mobile number page
@pytest.mark.SMMA_005
@pytest.mark.Android
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
def test_verify_redirect_to_setup_pin_by_using_valid_no():
    number = generate_random_integer(length=7, prefix='844')
    #LoginPage.launch_app_again()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no(number)
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no(number)
    LoginPage.enter_otp(user_data['valid_otp'])
    LoginPage.verify_setup_pin_page()