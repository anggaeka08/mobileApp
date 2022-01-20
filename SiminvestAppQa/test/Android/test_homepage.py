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
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(3)
        self.click_on_stock_code()
        self.verify_sdp_page()

    #Validate user is redirected to the tariik dana page when user clicks on tarik dana button for KYC verified user.
    @pytest.mark.H_SMMA_003
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirect_to_tarik_dana_on_click_of_btn(self):
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

    # Validate user is redirected to the Riwayaat page when user clicks on the riwayat button for KYC verified user.
    @pytest.mark.H_SMMA_004
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirect_to_riwayat_on_click_of_btn(self):
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
        self.click_on_riwayat_btn()
        self.verify_riwayat_page()

    # Validate the screen is properly visible and user is able to swipe up and swipe down the page.
    @pytest.mark.H_SMMA_005
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_swipe_up_and_down_on_homepage(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.scroll_up_to_down()
        self.scroll_down_to_up()

    # Verify the main button is grammatically correct Example.
    @pytest.mark.H_SMMA_006
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_grammatically_spelling(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.verify_spelling_on_homepage()

    #Validate user is redirected to the global search page and the keypad is open with caps alphabet when user click on global search bar button "Cari"
    @pytest.mark.H_SMMA_007
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_keyboard_is_open_after_click_on_global_search(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_global_search_btn()
        self.verify_keyboard_on_off()

    # Validate user is redirected to the registration page when new user click on the "register" or "login" "Daftar masuk" button.
    @pytest.mark.H_SMMA_008
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirection_for_new_user_to_the_register_page(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.set_pin(user_data['setup_pin_value'])
        #self.verify_risk_profile_page()
        #self.click_agresif_profile()
        self.close_home_page_banner()
        self.verify_home_page()
        self.click_on_Daftar_masuk()
        self.verify_registration_page()

    #Validate user User is redirected to "RDN balance" page when KYC verified user click on Saldo RDN button.
    @pytest.mark.H_SMMA_009
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_rdn_page_redirect_after_click_saldo_rdn(self):
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

    #Validate user is redirected to the "Top Up" instruction page when user click on the Top Up button for KYC verified user.
    @pytest.mark.H_SMMA_010
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_topup_page_from_rdn_page(self):
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
        self.click_on_top_up_btn()
        self.verify_topup_page()

    #Validate the refresh icon will appear at the top when user swipe down force fully and the page should refreshed.
    @pytest.mark.H_SMMA_011
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_refresh_homepage(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.scroll_up_to_down()
        self.verify_home_page_reg_user()

   # Validate user is redirected to indeks page when user click on indeks button.
    @pytest.mark.H_SMMA_012
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_indeks_page_redirection(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_indeks_btn()
        self.verify_indeks_page()

    # Validate user is redirected to list of sector page when user is clcik on sector button.
    @pytest.mark.H_SMMA_013
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_Sector_page_redirection(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_sector_button()
        self.verify_sector_page()

    # Validate user is redirected to event page when user click on events button.
    @pytest.mark.H_SMMA_014
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_Events_page_redirection(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_event_btn()
        self.verify_event_page()

    #Validate user is redirected to eIPO page when user click on eIPO button.
    @pytest.mark.H_SMMA_015
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_eIPO_page_redirection(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_eipo_btn()
        self.verify_eipo_page()
        self.verify_eipo_entry()

    #Validate user is able to see the Index value "IHSG" on the center of home screen.
    @pytest.mark.H_SMMA_019
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_homepage_stock_details(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.verify_homepage_stock()

    #Validate user is able to see the list of stock based on "Top Frequency" by default on quick stock status result section at square form.
    @pytest.mark.H_SMMA_021
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_homepage_Top_frequency_details(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.verify_top_frequency_presention()
        self.verify_stock_presence_in_top_frequency()