import pytest
from SiminvestAppQa.src.pages.login_page import LoginPage
from SiminvestAppQa.src.pages.home_page import HomePage
from SiminvestAppQa.src.utilities.BrowserStackUtilities import sync_app

LoginPage = LoginPage()
HomePage = HomePage()


@pytest.mark.ios
@pytest.mark.ios_SMMA_001
def test_login_with_valid_mobile_no():
    # sync_app()
    LoginPage.click_mulai_sekarang()
    LoginPage.type_mobile_no("8441234512")
    LoginPage.click_selanjutnya()
    LoginPage.enter_otp("1234")
    LoginPage.set_pin("123456")
    LoginPage.verify_risk_profile_page()
    LoginPage.click_agresif_profile()
    HomePage.verify_top_up()
