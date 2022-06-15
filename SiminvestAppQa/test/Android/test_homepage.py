import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time

@pytest.mark.usefixtures("unittest_setUpClass_fixture_homePage_test")
class homePage_test(HomePage,LoginPage):

    # Validate user is able open the SDP page via global search bar.
    @pytest.mark.H_SMMA_001
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_validate_global_search_for_stock(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(2)
        self.click_on_stock_code()
        self.verify_sdp_page()

    #Validate user is redirected to the tariik dana page when user clicks on tarik dana button for KYC verified user.
    @pytest.mark.H_SMMA_003
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirect_to_tarik_dana_on_click_of_btn(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
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
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
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
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.scroll_up()
        self.scroll_down()

    # Verify the main button is grammatically correct Example.
    @pytest.mark.H_SMMA_006
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_grammatically_spelling(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_spelling_on_homepage()

    #Validate user is redirected to the global search page and the keypad is open with caps alphabet when user click on global search bar button "Cari"
    @pytest.mark.H_SMMA_007
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_keyboard_is_open_after_click_on_global_search(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_global_search_btn()
        self.verify_keyboard_on_off()

    # Validate user is redirected to the registration page when new user click on the "register" or "login" "Daftar masuk" button.
    @pytest.mark.H_SMMA_008
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirection_for_new_user_to_the_register_page(self):
        number = generate_random_integer(length=7, prefix='844')
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.set_pin(user_data['setup_pin_value'])
        self.close_home_page_banner()
        self.verify_home_page()
        self.click_on_Daftar_masuk()
        self.verify_registration_page()

    #Validate user User is redirected to "RDN balance" page when KYC verified user click on Saldo RDN button.
    @pytest.mark.H_SMMA_009
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_rdn_page_redirect_after_click_saldo_rdn(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_saldo_rdn()
        self.sleep(3)
        self.verify_rdn_balance_page()

    #Validate user is redirected to the "Top Up" instruction page when user click on the Top Up button for KYC verified user.
    @pytest.mark.H_SMMA_010
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_topup_page_from_rdn_page(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
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
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.scroll_down()
        self.verify_home_page_reg_user()

   # Validate user is redirected to indeks page when user click on indeks button.
    @pytest.mark.H_SMMA_012
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_indeks_page_redirection(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_indeks_btn()
        self.verify_indeks_page()

    # Validate user is redirected to list of sector page when user is clcik on sector button.
    @pytest.mark.H_SMMA_013
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_Sector_page_redirection(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_sector_button()
        self.verify_sector_page()

    # Validate user is redirected to event page when user click on events button.
    @pytest.mark.H_SMMA_014
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_Events_page_redirection(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_event_btn()
        self.verify_event_page()

    #Validate user is redirected to eIPO page when user click on eIPO button.
    @pytest.mark.H_SMMA_015
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_eIPO_page_redirection(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_eipo_btn()
        self.verify_eipo_page()
        self.verify_eipo_entry()

    #Validate user is able to see the Index value "IHSG" on the center of home screen.
    @pytest.mark.H_SMMA_019
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_homepage_stock_details(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_homepage_stock()

    #Validate user is able to see the list of stock based on "Top Frequency" by default on quick stock status result section at square form.
    @pytest.mark.H_SMMA_021
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_homepage_Top_frequency_details(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_top_frequency_presention()
        self.verify_stock_presence_in_top_frequency()

    #Validate the half card is open of sort list of stock when user click on down arrow button right side of top frequency.
    @pytest.mark.H_SMMA_022
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_half_card_open_after_click_on_down_arrow(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_TF_down_arrow()
        self.verify_half_card_page()

    #Validate the half card can be close by swipe down and phone back button.
    @pytest.mark.H_SMMA_023
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_close_half_card_open_by_back_btn(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_TF_down_arrow()
        self.verify_half_card_page()
        self.go_back()
        self.verify_home_page_reg_user()

    #Validate user is redirected to mover page to add the stock when user click on the see more button available on extreme right side of top frequency category button.
    @pytest.mark.H_SMMA_024
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_mover_page(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_see_more_btn()
        self.verify_mover_page()

    #Validate user is redirected to watchlist half card page when user is clicks on the watchlist name or ( Default ) button.
    @pytest.mark.H_SMMA_025
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_watchlist_half_card(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.scroll_up()
        self.click_on_default_btn()
        self.verify_watchlist_card()
        self.verify_watchlist_details()

    #validate user is able to close the half card by swipe down and back button when user open the watchlist half card page.
    @pytest.mark.H_SMMA_026
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_watchlist_half_card_close_by_back_btn(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.scroll_up()
        self.click_on_default_btn()
        self.verify_watchlist_card()
        self.verify_watchlist_details()
        self.go_back()
        #self.verify_home_page_reg_user()

    # Validate user is able to see the portfolio value with green color at center of the screen when user has completed the signup or KYC verified.
    @pytest.mark.H_SMMA_028
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_location_of_portfolio(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_portfolio_on_homepage()

    # Validate user is able to see the buying power value at center of the screen when user has completed the signup or KYC verified.
    @pytest.mark.H_SMMA_029
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_location_of_buying_power(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_portfolio_on_homepage()

    #Validate user is redirected to Top up page when user click on Topup button.
    @pytest.mark.H_SMMA_030
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_top_up_page_redirection_from_homepage(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_top_up_from_homepage()
        self.verify_topup_page()

    #Validate user is redirected to the SDP when user click on the company name under "Top Frequency" list.
    @pytest.mark.H_SMMA_031
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_sdp_from_top_frequecny_list(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_stock_1_from_top_frequency_list()
        self.sleep(3)
        self.verify_sdp_page_from_top_freqency_list()

    #Validate user is redirected to the SDP when user click on the company name under "Default watchlist" list.
    @pytest.mark.H_SMMA_032
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_sdp_watchlist_entry(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.scroll_up()
        self.click_on_default_watchlist_entry_1()
        self.verify_sdp_page_from_top_freqency_list()

    #Validate user redirected on home page when user click on back button of app and of phone when user is on SDP page.
    @pytest.mark.H_SMMA_033
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_back_btn_from_sdp_page_of_watchlist(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.scroll_up()
        self.click_on_default_watchlist_entry_1()
        self.verify_sdp_page_from_top_freqency_list()
        self.go_back()
        self.sleep(10)
        self.verify_home_page_reg_user_after_back_from_watchlist_new()

    #Validate user is redirected to research page when user click on the research button.
    @pytest.mark.H_SMMA_034
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_redirection_on_research_page(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_research_page()

    # Validate user is redirected to the stock signal page of the stock signal when user click on the research button.
    @pytest.mark.H_SMMA_035
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_stock_signal_presence_on_research_page(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_stock_signal_on_research_page()

    #Validate user is gets out from the app when user clicks on the back button when user is on the research page.
    @pytest.mark.H_SMMA_036
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_back_button_on_research_page(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        #self.verify_stock_signal_on_research_page()
        self.go_back()
        self.check_phone_home_screen()

    #* Validate user is redirected to the invest now page when user click on the portfolio page when is non KYC user.
    @pytest.mark.H_SMMA_037
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_portfolio_page_for_non_kyc_user(self):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_non_kyc_user()

    #Validate user is able to see the portfolio page when user click on the portfolio button when user is kYC verified user.
    @pytest.mark.H_SMMA_038
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_portfolio_page_for_kyc_user(self):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()

    #Validate user is redirected to transaction page when user click on the transaction button.
    @pytest.mark.H_SMMA_039
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_transaction_page_kyc_user(self):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_transaction_btn()
        self.verify_transaction_page()

    #Validate user is redirected to profile page when user click on the profile page button.
    @pytest.mark.H_SMMA_040
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_profile_page_kyc_user(self):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_profile_btn()
        self.verify_profile_page()

    #Validate user should see his name as Hi, Test on the top left corner if he has completed the signup or KYC verified.
    @pytest.mark.H_SMMA_041
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_verify_username_on_homepage_page_user(self):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.verify_username_on_homepage()