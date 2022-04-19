import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time


@pytest.mark.usefixtures("unittest_setUpClass_fixture_signUpFlow_test")
class signUpFlow_test(LoginPage):

    # Verify non redirection while entering wrong phone no and otp and verify login success with correct number
    @pytest.mark.signup_SMMA_001_002_003
    @pytest.mark.Android
    @pytest.mark.signupFlow
    def test_validate_smma_001_002_003(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(str(generate_random_integer(8)))
        self.click_selanjutnya()
        self.verify_mobile_no_page()
        number =  generate_random_integer(length=7, prefix='844')
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp('1235')
        self.verify_otp_page_with_phone_no(number)
        self.enter_otp('1234')
        self.set_pin('123456')
        self.close_home_page_banner()
        self.verify_home_page()

    #Validate application should not respond anything when user enter 5 digit PIN.
    @pytest.mark.signup_SMMA_004
    @pytest.mark.Android
    @pytest.mark.signupFlow
    def test_validate_appliction_action_after_enter_5_digit_pin(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.set_pin('12345')
        self.verify_setup_pin_page()

    #Validate user should redirect to enter OTP page when  user change the mobile number.
    @pytest.mark.signup_SMMA_005
    @pytest.mark.Android
    @pytest.mark.signupFlow
    def test_validate_redirection_to_otp_page_when_re_enter_phone_no(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.click_back_button_otp_page()
        number_1 = generate_random_integer(length=7, prefix='844')
        self.type_mobile_no(number_1)
        self.click_selanjutnya()
        self.verify_otp_page_with_phone_no(number_1)

    # Validate user is able to login after user click on resend OTP page
    @pytest.mark.signup_SMMA_006
    @pytest.mark.Android
    @pytest.mark.signupFlow
    def test_validate_signup_after_resend_otp(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        time.sleep(35)
        self.click_Kirim_Ulang()
        self.enter_otp('1234')
        self.set_pin('123456')
        self.close_home_page_banner()
        self.verify_home_page()

    # Validate user is able to login with correct details
    @pytest.mark.signup_SMMA_010
    @pytest.mark.Android
    @pytest.mark.signupFlow
    def test_validate_login_with_correct_details(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.set_pin('123456')
        self.close_home_page_banner()
        self.verify_home_page()
