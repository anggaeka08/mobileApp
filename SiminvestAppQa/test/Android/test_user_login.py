import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage

LoginPage = LoginPage()
HomePage = HomePage()

#Test cases for login with valid new number
@pytest.mark.SMMA_001
@pytest.mark.Android
def test_login_with_valid_mobile_no():
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8441234587")
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