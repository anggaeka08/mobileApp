import pytest
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data
import logging as logger


@pytest.mark.usefixtures("unittest_setUpClass_fixture_SDP_test")
class SDP_test(StockDetailPage, BuyProcess):

    # Validate user is able to star mark the stock/ Validate user is able to un-mark the star.
    @pytest.mark.SDP_SMMA_001_002
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_star_mark_on_sdp(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.scroll_down()
        self.tap_on_star()
        self.click_on_watchlist()
        self.sleep(2)
        self.go_back()
        self.go_back()
        self.sleep(2)
        self.scroll_up()
        self.verify_stock_on_watchlist(True)
        self.click_on_stock()
        self.tap_on_star()
        self.click_on_watchlist()
        self.go_back()
        self.scroll_ups()
        self.verify_stock_on_watchlist(False)

    # Validate search option on sdp page
    @pytest.mark.SDP_SMMA_003_004
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_star_mark_on_sdp(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.click_on_search_btn()
        self.enter_stock_code('ACES')
        self.click_on_stocks()
        self.verify_sdp_page()
        self.go_back()
        self.go_back()
        self.verify_home_page_reg_user()

    # Validate test cases SMMA_013
    @pytest.mark.SDP_SMMA_006_013
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Validate_test_cases_SMMA_006_013(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.chart_presence()
        self.order_book_tab_open()

  # Validate test cases  SMMA_016_021_022
    @pytest.mark.SDP_SMMA_016_021_022
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Validate_profile_btn_and_header_details_of_values(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_details_down_to_beli_btn()
        self.click_on_profile()
        self.scroll_up()
        self.verify_details_of_profile_tab()
        self.verify_stock_company_address()

    #Validate news tab on SDP page and news page details
    @pytest.mark.SDP_SMMA_023_to_027
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Validate_news_tab_on_SDP_page_and_news_page_details(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_news_availability_on_sdp()
        self.click_on_news()
        self.scroll_up_screen()
        self.verify_news_dates_list()
        self.verify_news_title()
        self.validate_domain_name_for_one_news()

    #Validate news tab on SDP page and news page details
    @pytest.mark.SDP_SMMA_028_to_031
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Validate_news_tab_on_SDP_pages(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_news_availability_on_sdp()
        self.click_on_news()
        self.scroll_up_screen()
        self.validate_maximum_available_news()
        self.validate_all_news_are_separated()

    # Validate user is redirected to customer care support page when user click on contact customer button available at the bottom on external browser.
    @pytest.mark.SDP_SMMA_45
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Validate_redirection_after_click_on_customer_support_btn(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.scroll_up_screen()
        self.verify_redirection_after_click_on_support_btn()

    #Validate test cases  SMMA_014
    @pytest.mark.SDP_SMMA_014
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_profile_details_for_stock_company_details_unavailable(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'WIFI-W')
        self.verify_details_down_to_beli_btn()
        self.click_on_profile()
        self.verify_stock_profile_when_details_not_available()

    #Validate test cases  SMMA_037
    @pytest.mark.SDP_SMMA_037
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_user_will_able_to_see_value_at_below_of_the_stock_price(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.verify_details_availability_when_move_to_sdp_by_portfolio_page()

