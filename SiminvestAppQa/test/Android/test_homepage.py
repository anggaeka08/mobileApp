import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time


class homePage_test(LoginPage, HomePage):

    # Validate user is able open the SDP page via global search bar.
    @pytest.mark.SMMA_001
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_validate_global_search_for_stock(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        # LoginPage.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_global_search_btn('ACES')
        self.sleep(3)
        self.click_on_stock_code()
        self.verify_sdp_page()
