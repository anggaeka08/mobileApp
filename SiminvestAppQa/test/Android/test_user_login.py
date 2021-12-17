import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time

LoginPage = LoginPage()
HomePage = HomePage()

#Test cases for login with valid new number
@pytest.mark.SMMA_001
@pytest.mark.Android
def test_login_with_valid_mobile_no():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8441245882")
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp("1234")
    LoginPage.set_pin("123456")
    LoginPage.verify_risk_profile_page()
    LoginPage.click_agresif_profile()
    LoginPage.verify_home_page()

#Test case for login with reg Number
@pytest.mark.SMMA_002
@pytest.mark.Android
def test_login_with_invalid_no_less_then_10():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("808343")
    LoginPage.verify_selanjutnya()

#Test case for
@pytest.mark.SMMA_003
@pytest.mark.Android
def test_login_with_valid_reg_mobile_no():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8445557108")
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp("1234")
    LoginPage.enter_pin()
    LoginPage.verify_home_page_reg_user()

#Test case for received again otp
@pytest.mark.SMMA_009
@pytest.mark.Android
def test_did_not_receive_the_otp():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8445557108")
    LoginPage.click_selanjutnya()
    time.sleep(35)
    LoginPage.click_Kirim_Ulang()

#Test case for re-enter phone no by back after otp page
@pytest.mark.SMMA_010
@pytest.mark.Android
def test_did_not_receive_the_otp():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8445557108")
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no("8445557108")
    LoginPage.click_back_button_otp_page()
    LoginPage.type_mobile_no("8445557190")
    LoginPage.click_selanjutnya()
    LoginPage.verify_otp_page_with_phone_no("8445557190")
