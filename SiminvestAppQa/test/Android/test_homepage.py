import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time

@pytest.mark.usefixtures("_unittest_setUpClass_fixture_homePage_test")
class homePage_test(HomePage,LoginPage):

    # Validate user is able open the SDP page via global search bar.
    @pytest.mark.GlobalSaerchOption
    @pytest.mark.Homepage
    @pytest.mark.Android
    @allure.story("F-5:HomePage Feature")
    def test_validate_global_search_for_stock(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.validate_text_in_global_search_before_click()
        self.click_global_search_btn()
        self.Validate_text_and_keyboard_on_after_click_in_global_search()
        self.validate_search_entry_for_invalid_stock_and_saham_text()
        self.go_back()
        self.go_back()
        self.validate_text_in_global_search_before_click()
        self.click_global_search_btn()
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(2)
        self.validate_saham_header_and_stock_code_and_stock_name('ACES')
        self.click_on_stock_code()
        self.verify_sdp_page()
        self.go_back()
        self.sleep(2)
        self.validate_saham_header_and_stock_code_and_stock_name('ACES')
        self.click_global_search_btn_and_saerch_stock('A')
        self.sleep(3)
        self.validate_saham_header_and_stock_code_and_stock_name('A')
        self.click_global_search_btn_and_saerch_stock('Simas Saham Bertumbuh')
        self.sleep(3)
        self.validate_MF_search_in_global_search_and_Redirection_after_click()




