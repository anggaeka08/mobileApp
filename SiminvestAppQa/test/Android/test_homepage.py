import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time


class homePage_test(LoginPage, HomePage):

    # Validate user is able open the SDP page via global search bar.
    @pytest.mark.H_SMMA_001
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

    #Validate user is redirected to the tariik dana page when user clicks on tarik dana button for KYC verified user.
    @pytest.mark.H_SMMA_003
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirect_to_tarik_dana_on_click_of_btn(self):
       # self.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_saldo_rdn()
        self.sleep(3)
        self.verify_rdn_balance_page()
        self.click_on_tarik_dana_btn()
        self.verify_tarik_dana_page()
